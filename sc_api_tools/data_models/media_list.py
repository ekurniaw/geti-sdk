from __future__ import annotations

from collections import UserList
from typing import List, Dict, Any, Type, TypeVar, cast, Generic

from omegaconf import OmegaConf

from sc_api_tools.data_models.media import MediaItem, Video, Image, VideoFrame

MediaTypeVar = TypeVar("MediaTypeVar", Image, Video, VideoFrame)


class MediaList(UserList, Generic[MediaTypeVar]):
    """
    A list containing SC media entities
    """
    @property
    def ids(self) -> List[str]:
        """
        Returns a list of unique database IDs for all media items in the media list

        :return:
        """
        return [item.id for item in self.data]

    @property
    def names(self) -> List[str]:
        """
        Returns a list of filenames for all media items in the media list

        :return:
        """
        return [item.name for item in self.data]

    def get_by_id(self, id_value: str) -> MediaItem:
        """
        Returns the item with id `id_value` from the media list

        :return: MediaItem with database ID corresponding to 'id_value'
        """
        for item in self.data:
            if item.id == id_value:
                return item
        raise ValueError(
            f"Media list {self} does not contain item with ID {id_value}."
        )

    def get_by_filename(self, filename: str) -> MediaItem:
        """
        Returns the item with name `filename` from the media list

        :return: MediaItem with name corresponding to 'filename'
        """
        for item in self.data:
            if item.name == filename:
                return item
        raise ValueError(
            f"Media list {self} does not contain item with filename {filename}."
        )

    @property
    def media_type(self) -> Type[MediaTypeVar]:
        """
        Returns the type of the media contained in this list.

        :return:
        """
        if self.data:
            return type(self.data[0])
        else:
            raise ValueError("Cannot deduce media type from empty MediaList")

    @staticmethod
    def from_rest_list(
            rest_input: List[Dict[str, Any]],
            media_type: Type[MediaTypeVar]
    ) -> MediaList[MediaTypeVar]:
        """
        Creates a MediaList instance from a list of media entities obtained from the
        SC /media endpoints

        :param rest_input: List of dictionaries representing media entities in SC
        :param media_type: Image or Video, type of the media entities that are to be
            converted.

        :return: MediaList holding the media entities contained in `rest_input`,
            where each entity is of type `media_type`
        """
        output_list = MediaList[MediaTypeVar]([])
        for media_dict in rest_input:
            media_dict_config = OmegaConf.create(media_dict)
            schema = OmegaConf.structured(media_type)
            config = OmegaConf.merge(schema, media_dict_config)
            object = cast(media_type, OmegaConf.to_object(config))
            output_list.append(object)
        return output_list
