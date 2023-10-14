# coding: utf-8

"""
    GeoServer Namespace

    A namespace is a uniquely identifiable grouping of feature types. It is identified by a prefix and a URI.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.namespaces_api import NamespacesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNamespacesApi(unittest.TestCase):
    """NamespacesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.namespaces_api.NamespacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_namespace(self):
        """Test case for delete_namespace

        Delete a namespace  # noqa: E501
        """
        pass

    def test_delete_namespaces(self):
        """Test case for delete_namespaces

        """
        pass

    def test_get_namespace(self):
        """Test case for get_namespace

        Retrieve a namespace  # noqa: E501
        """
        pass

    def test_get_namespaces(self):
        """Test case for get_namespaces

        Get a list of namespaces  # noqa: E501
        """
        pass

    def test_post_namespace(self):
        """Test case for post_namespace

        """
        pass

    def test_post_namespaces(self):
        """Test case for post_namespaces

        Add a new namespace to GeoServer  # noqa: E501
        """
        pass

    def test_put_namespace(self):
        """Test case for put_namespace

        Update a namespace  # noqa: E501
        """
        pass

    def test_put_namespaces(self):
        """Test case for put_namespaces

        """
        pass


if __name__ == '__main__':
    unittest.main()
