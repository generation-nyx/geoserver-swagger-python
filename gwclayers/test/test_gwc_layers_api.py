# coding: utf-8

"""
    GeoWebCache Layers

    A layer is a published resource (feature type or coverage).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.gwc_layers_api import GwcLayersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGwcLayersApi(unittest.TestCase):
    """GwcLayersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.gwc_layers_api.GwcLayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_layers_get(self):
        """Test case for layers_get

        Get a list of cached layers  # noqa: E501
        """
        pass

    def test_layers_name_delete(self):
        """Test case for layers_name_delete

        Delete cached layer  # noqa: E501
        """
        pass

    def test_layers_name_get(self):
        """Test case for layers_name_get

        Retrieve a cached layer  # noqa: E501
        """
        pass

    def test_layers_name_post(self):
        """Test case for layers_name_post

        Modify a cached layer (Deprecated).  # noqa: E501
        """
        pass

    def test_layers_name_put(self):
        """Test case for layers_name_put

        Create or update a cached layer.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
