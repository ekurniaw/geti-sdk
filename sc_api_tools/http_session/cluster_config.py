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

from dataclasses import dataclass
from typing import Dict, Optional

DEFAULT_API_VERSION = "v1"
LEGACY_API_VERSION = "v1.0"


@dataclass
class ClusterConfig:
    """
    Configuration for requests sessions, with host, username and password.

    :var host: full hostname or ip address of the SC instance.
        Note: this should include the protocol (i.e. https://your_sc_hostname.com)
    :var username: Username to log in to the instance.
    :var password: Password required to log in to the instance
    :var has_valid_certificate: Set to True if the server has a valid SSL certificate
        that should be validated and used to establish an encrypted HTTPS connection
    :var proxies: Optional dictionary containing proxy information, if this is
        required to connect to the SC server. For example:

        proxies = {
            'http': http://proxy-server.com:<http_port_number>,
            'https': http://proxy-server.com:<https_port_number>
        },

        if set to None (the default), the global proxy settings found on the system
        will be used. If set to an emtpy dictionary, no proxy will be used.
    """

    host: str
    username: str
    password: str
    has_valid_certificate: bool = False
    proxies: Optional[Dict[str, str]] = None

    def __post_init__(self):
        """
        Initialize private attributes
        """
        self._api_version = DEFAULT_API_VERSION

    @property
    def base_url(self) -> str:
        """
        Return the base UR for accessing the cluster.
        """
        return f"{self.host}/api/{self.api_version}/"

    @property
    def api_version(self) -> str:
        """
        Return the api version string to be used in the URL for making REST requests.
        """
        return self._api_version

    @api_version.setter
    def api_version(self, value: str) -> None:
        """
        Set the api_version string to be used in the URL for making REST requests.
        """
        if not value.startswith("v"):
            raise ValueError(
                "API version string should follow the format: 'vX', where X is the "
                "(integer) version number, e.g.: 'v1', 'v2', 'v3'."
            )
        self._api_version = value

    @property
    def api_pattern(self) -> str:
        """
        Return the API pattern used in the URL
        """
        return f"/api/{self.api_version}/"
