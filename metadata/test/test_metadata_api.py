# coding: utf-8

"""
    GeoServer Metadata Community Module

    Customized Metadata Bulk Operations.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.metadata_api import MetadataApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.metadata_api.MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_metadata_delete(self):
        """Test case for metadata_delete

        Delete all custom metadata  # noqa: E501
        """
        pass

    def test_metadata_fix_get(self):
        """Test case for metadata_fix_get

        Fix all custom metadata  # noqa: E501
        """
        pass

    def test_metadata_import_post(self):
        """Test case for metadata_import_post

        Bulk import from geonetwork and/or template linking.  # noqa: E501
        """
        pass

    def test_metadata_native_to_custom_get(self):
        """Test case for metadata_native_to_custom_get

        Perform native-to-custom mapping for all layers.  # noqa: E501
        """
        pass

    def test_metadata_native_to_custom_post(self):
        """Test case for metadata_native_to_custom_post

        Perform native-to-custom mapping for selected layers.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
