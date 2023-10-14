# coding: utf-8

"""
    GeoServer Logging

    The Logging area shows logging options for the server  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.logging_api import LoggingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLoggingApi(unittest.TestCase):
    """LoggingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.logging_api.LoggingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_logging(self):
        """Test case for get_logging

        Get logging configuration of GeoServer  # noqa: E501
        """
        pass

    def test_put_logging(self):
        """Test case for put_logging

        Update logging  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()