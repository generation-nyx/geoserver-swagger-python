# coding: utf-8

"""
    GeoServer Settings

    The Settings area shows global configuration for the server  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.settings_api import SettingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_contact_settings(self):
        """Test case for delete_contact_settings

        """
        pass

    def test_delete_settings(self):
        """Test case for delete_settings

        """
        pass

    def test_delete_workspace_settings(self):
        """Test case for delete_workspace_settings

        """
        pass

    def test_get_contact_settings(self):
        """Test case for get_contact_settings

        Get a list of all global contact settings  # noqa: E501
        """
        pass

    def test_get_settings(self):
        """Test case for get_settings

        Get a list of all global settings  # noqa: E501
        """
        pass

    def test_get_workspace_settings(self):
        """Test case for get_workspace_settings

        Get a list of all workspace-specific settings  # noqa: E501
        """
        pass

    def test_post_contact_settings(self):
        """Test case for post_contact_settings

        """
        pass

    def test_post_settings(self):
        """Test case for post_settings

        """
        pass

    def test_post_workspace_settings(self):
        """Test case for post_workspace_settings

        Create workspace-specific settings  # noqa: E501
        """
        pass

    def test_put_contact_settings(self):
        """Test case for put_contact_settings

        Update contact settings  # noqa: E501
        """
        pass

    def test_put_settings(self):
        """Test case for put_settings

        Update settings  # noqa: E501
        """
        pass

    def test_put_workspace_settings(self):
        """Test case for put_workspace_settings

        Update workspace-specific settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
