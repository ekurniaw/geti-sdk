# Copyright (C) 2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.
import logging
import os
import time
from glob import glob
from typing import (
    Any,
    BinaryIO,
    ClassVar,
    Dict,
    Generic,
    List,
    Optional,
    Sequence,
    Type,
)

from tqdm.auto import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from geti_sdk.data_models import Image, MediaType, Project, Video, VideoFrame
from geti_sdk.data_models.containers.media_list import MediaList, MediaTypeVar
from geti_sdk.data_models.enums.media_type import (
    SUPPORTED_IMAGE_FORMATS,
    SUPPORTED_VIDEO_FORMATS,
)
from geti_sdk.data_models.project import Dataset
from geti_sdk.data_models.utils import numpy_from_buffer
from geti_sdk.http_session import GetiRequestException, GetiSession
from geti_sdk.rest_clients.dataset_client import DatasetClient
from geti_sdk.rest_converters.media_rest_converter import MediaRESTConverter

MEDIA_TYPE_MAPPING = {MediaType.IMAGE: Image, MediaType.VIDEO: Video}
MEDIA_SUPPORTED_FORMAT_MAPPING = {
    MediaType.IMAGE: SUPPORTED_IMAGE_FORMATS,
    MediaType.VIDEO: SUPPORTED_VIDEO_FORMATS,
}
MEDIA_DOWNLOAD_FORMAT_MAPPING = {MediaType.IMAGE: ".jpg", MediaType.VIDEO: ".mp4"}


class BaseMediaClient(Generic[MediaTypeVar]):
    """
    Class to manage media up and downloads for a certain project.
    """

    _MEDIA_TYPE: ClassVar[MediaType]

    def __init__(self, session: GetiSession, workspace_id: str, project: Project):
        self.session = session
        self._workspace_id = workspace_id
        self._base_url = f"workspaces/{workspace_id}/projects/{project.id}/datasets"
        self._project = project
        self.__media_type: Type[MediaTypeVar] = self.__get_media_type(self._MEDIA_TYPE)
        self._dataset_client = DatasetClient(
            session=session, project=project, workspace_id=workspace_id
        )

    def base_url(self, dataset: Dataset) -> str:
        """
        Return the base url for the media endpoint.

        :param dataset: Dataset to retrieve the base url for
        :return: string containing the base url
        """
        return f"{self._base_url}/{dataset.id}/media/{self.plural_media_name}"

    @property
    def plural_media_name(self) -> str:
        """
        Convert the type of the media entities managed by this media client to a
        string in plural form.

        :return:
        """
        return f"{self._MEDIA_TYPE}s"

    @staticmethod
    def __get_media_type(media_type: MediaType) -> Type[MediaTypeVar]:
        """
        Get the type of the media entities that are managed by this media client.

        :param media_type: MediaType Enum instance representing the type of media
            entities
        :return: Type of media entities that can be used to instantiate objects of this
            type
        """
        return MEDIA_TYPE_MAPPING[media_type]

    def _get_all(self, dataset: Optional[Dataset] = None) -> MediaList[MediaTypeVar]:
        """
        Get a list holding all media entities of a certain type in the project.

        :param dataset: Optional dataset to retrieve the media for. If no dataset is
            specified, only media from the training dataset will be returned
        :return: MediaList holding all media of a certain type in the project
        """
        if dataset is None:
            dataset = self._project.training_dataset

        response = self.session.get_rest_response(
            url=f"{self.base_url(dataset=dataset)}?top=500", method="GET"
        )
        total_number_of_media: int = response["media_count"][self.plural_media_name]
        raw_media_list: List[Dict[str, Any]] = []
        while len(raw_media_list) < total_number_of_media:
            for media_item_dict in response["media"]:
                raw_media_list.append(media_item_dict)
            if "next_page" in response.keys():
                response = self.session.get_rest_response(
                    url=response["next_page"], method="GET"
                )
        return MediaList.from_rest_list(
            rest_input=raw_media_list, media_type=self.__media_type
        )

    def _delete_media(self, media_list: Sequence[MediaTypeVar]) -> bool:
        """
        Delete all media entities in `media_list` from the project.

        :param media_list: List of media entities to delete
        :return: True if all items on the media list were deleted successfully,
            False otherwise
        """
        if not isinstance(media_list, MediaList) and isinstance(media_list, Sequence):
            media_list = MediaList(media_list)
        if media_list.media_type == VideoFrame:
            raise ValueError("Unable to delete individual video frames.")
        logging.info(
            f"Deleting {len(media_list)} {self.plural_media_name} from project "
            f"'{self._project.name}'..."
        )
        for media_item in media_list:
            try:
                self.session.get_rest_response(url=media_item.base_url, method="DELETE")
            except GetiRequestException as error:
                if error.status_code == 409:
                    logging.info(
                        f"Project '{self._project.name}' is locked for deletion, "
                        f"unable to delete media. Aborting deletion."
                    )
                    return False
                if error.status_code == 404 or error.status_code == 204:
                    # Media item has already been deleted, continue with the rest of
                    # the list
                    continue
        return True

    def _upload_bytes(
        self, buffer: BinaryIO, dataset: Optional[Dataset] = None
    ) -> Dict[str, Any]:
        """
        Upload a buffer representing a media file to the server.

        :param buffer: BinaryIO object representing a media file
        :param dataset: Dataset to upload the media to. If no dataset is passed, the
            media will be uploaded into the default (training) dataset
        :return: Dictionary containing the response of the Intel® Geti™ server, which
            holds the details of the uploaded entity
        """
        if dataset is None:
            dataset = self._project.training_dataset
        response = self.session.get_rest_response(
            url=f"{self.base_url(dataset)}",
            method="POST",
            contenttype="multipart",
            data={"file": buffer},
        )
        return response

    def _upload(
        self, filepath: str, dataset: Optional[Dataset] = None
    ) -> Dict[str, Any]:
        """
        Upload a media file to the server.

        :param filepath: full path to the media file on disk
        :param dataset: Dataset to upload the media to. If no dataset is passed, the
            media will be uploaded into the default (training) dataset
        :return: Dictionary containing the response of the Intel® Geti™ server, which
            holds the details of the uploaded entity
        """
        media_bytes = open(filepath, "rb")
        return self._upload_bytes(media_bytes, dataset=dataset)

    def _upload_loop(
        self,
        filepaths: List[str],
        skip_if_filename_exists: bool = False,
        dataset: Optional[Dataset] = None,
    ) -> MediaList[MediaTypeVar]:
        """
        Upload media from a list of filepaths. Also checks if media items with the same
        filename exist in the project, to make sure no duplicate items are uploaded.

        :param filepaths: List of full filepaths for media that should be
            uploaded
        :param skip_if_filename_exists: Set to True to skip uploading of a media item
            if a media item with the same filename already exists in the dataset.
            Defaults to False
        :param dataset: Dataset to upload the media to. If no dataset is passed, the
            media will be uploaded into the default (training) dataset
        :return: MediaList containing a list of all media entities that were uploaded
            to the project
        """
        if dataset is None:
            dataset = self._project.training_dataset
        media_in_project = self._get_all(dataset=dataset)
        uploaded_media: MediaList[MediaTypeVar] = MediaList[MediaTypeVar]([])
        upload_count = 0
        skip_count = 0
        logging.info(
            f"Starting {self._MEDIA_TYPE} upload to dataset '{dataset.name}'..."
        )
        tqdm_prefix = f"Uploading {self.plural_media_name}"

        t_start = time.time()
        with logging_redirect_tqdm(tqdm_class=tqdm):
            for filepath in tqdm(filepaths, desc=tqdm_prefix):
                name, ext = os.path.splitext(os.path.basename(filepath))
                if name in media_in_project.names and skip_if_filename_exists:
                    skip_count += 1
                    continue
                media_dict = self._upload(filepath=filepath, dataset=dataset)
                media_item = MediaRESTConverter.from_dict(
                    input_dict=media_dict, media_type=self.__media_type
                )
                if isinstance(media_item, Video):
                    media_item._data = filepath
                media_in_project.append(media_item)
                uploaded_media.append(media_item)
                upload_count += 1

        t_elapsed = time.time() - t_start
        if upload_count > 0:
            msg = (
                f"Upload complete. Uploaded {upload_count} new "
                f"{self.plural_media_name} in {t_elapsed:.1f} seconds."
            )
        else:
            msg = f"No new {self.plural_media_name} were uploaded."
        if skip_count > 0:
            msg = (
                msg + f" Found {skip_count} {self.plural_media_name} that already "
                f"existed in project, these {self.plural_media_name} were"
                f" skipped."
            )
        logging.info(msg)
        return uploaded_media

    def _upload_folder(
        self,
        path_to_folder: str,
        n_media: int = -1,
        skip_if_filename_exists: bool = False,
        dataset: Optional[Dataset] = None,
    ) -> MediaList[MediaTypeVar]:
        """
        Upload all media in a folder to the project. Returns the mapping of filenames
        to the unique IDs assigned by Sonoma Creek.

        :param path_to_folder: Folder with media items to upload
        :param n_media: Number of media to upload from folder
        :param skip_if_filename_exists: Set to True to skip uploading of a media item
            if a media item with the same filename already exists in the project.
            Defaults to False
        :param dataset: Dataset to upload the media to. If no dataset is passed, the
            media will be uploaded into the default (training) dataset
        :return: MediaList containing a list of all media entities that were uploaded
            to the project
        """
        media_formats = MEDIA_SUPPORTED_FORMAT_MAPPING[self._MEDIA_TYPE]
        filepaths: List[str] = []
        for media_extension in media_formats:
            filepaths += glob(
                os.path.join(path_to_folder, "**", f"*{media_extension}"),
                recursive=True,
            )
        n_files = len(filepaths)
        if n_media == -1:
            n_to_upload = n_files
        elif n_media < -1:
            raise ValueError(
                f"Number of {self.plural_media_name} to upload must positive, or -1 "
                f"to signify uploading all files in the folder. "
            )
        else:
            n_to_upload = n_files if n_files < n_media else n_media
        return self._upload_loop(
            filepaths=filepaths[0:n_to_upload],
            skip_if_filename_exists=skip_if_filename_exists,
            dataset=dataset,
        )

    def _download_all(
        self, path_to_folder: str, append_media_uid: bool = False
    ) -> None:
        """
        Download all media entities in a project to a folder on the local disk.

        :param path_to_folder: path to the folder in which the media should be saved
        :param append_media_uid: True to append the UID of a media item to the
            filename (separated from the original filename by an underscore, i.e.
            '{filename}_{media_id}').
        :return:
        """
        datasets = self._dataset_client.get_all_datasets()
        if len(datasets) == 1:
            # 1 dataset in project, do not split media in separate folder per dataset
            path_to_media_folder = os.path.join(path_to_folder, self.plural_media_name)
            self._download_dataset(
                dataset=datasets[0],
                path_to_media_folder=path_to_media_folder,
                append_media_uid=append_media_uid,
            )
        else:
            # Multiple datasets in the project, create a subfolder for media in each
            # dataset
            for dataset in datasets:
                path_to_media_folder = os.path.join(
                    path_to_folder, self.plural_media_name, dataset.name
                )
                self._download_dataset(
                    dataset=dataset,
                    path_to_media_folder=path_to_media_folder,
                    append_media_uid=append_media_uid,
                )

    def _download_dataset(
        self,
        dataset: Dataset,
        path_to_media_folder: str,
        append_media_uid: bool = False,
    ):
        """
        Download all media items of a single type in the dataset to a folder on disk

        :param dataset: Dataset to download the media for
        :param path_to_media_folder: path to the folder in which the media should be
            saved
        :param append_media_uid: True to append the UID of a media item to the
            filename (separated from the original filename by an underscore, i.e.
            '{filename}_{media_id}').
        """
        media_list = self._get_all(dataset=dataset)
        os.makedirs(path_to_media_folder, exist_ok=True, mode=0o770)
        logging.info(
            f"Downloading {len(media_list)} {self.plural_media_name} from project "
            f"'{self._project.name}' and dataset '{dataset.name}' to folder "
            f"{path_to_media_folder}..."
        )
        t_start = time.time()
        download_count = 0
        existing_count = 0
        tqdm_prefix = f"Downloading {self.plural_media_name}"
        with logging_redirect_tqdm(tqdm_class=tqdm):
            for media_item in tqdm(media_list, desc=tqdm_prefix):
                uid_string = ""
                if append_media_uid:
                    uid_string = f"_{media_item.id}"
                media_filepath = os.path.join(
                    path_to_media_folder,
                    os.path.basename(media_item.name)
                    + uid_string
                    + MEDIA_DOWNLOAD_FORMAT_MAPPING[self._MEDIA_TYPE],
                )
                if os.path.exists(media_filepath) and os.path.isfile(media_filepath):
                    existing_count += 1
                    continue
                response = self.session.get_rest_response(
                    url=media_item.download_url, method="GET", contenttype="jpeg"
                )

                with open(media_filepath, "wb") as f:
                    f.write(response.content)
                if isinstance(media_item, (Image, VideoFrame)):
                    # Set the numpy data attribute if the media item supports it
                    media_item._data = numpy_from_buffer(response.content)
                elif isinstance(media_item, Video):
                    media_item._data = media_filepath
                download_count += 1
        t_elapsed = time.time() - t_start
        if download_count > 0:
            msg = (
                f"Downloaded {download_count} {self.plural_media_name} in "
                f"{t_elapsed:.1f} seconds."
            )
        else:
            msg = f"No {self.plural_media_name} were downloaded."
        if existing_count > 0:
            msg += (
                f" {existing_count} existing {self.plural_media_name} were found "
                f"in the target folder, download was skipped for these "
                f"{self.plural_media_name}."
            )
        logging.info(msg)
