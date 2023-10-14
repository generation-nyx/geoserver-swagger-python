# coding: utf-8

"""
    GeoServer Parameter Extractor

    A parameter extractor rule allows specific request parameters as URL path fragments instead of using the query string. A echo parameter makes sure that certain URL paratemers are added to the capabilities documents backlinks.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.params_extractor_api import ParamsExtractorApi  # noqa: E501
from swagger_client.rest import ApiException


class TestParamsExtractorApi(unittest.TestCase):
    """ParamsExtractorApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.params_extractor_api.ParamsExtractorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_echo_parameter(self):
        """Test case for delete_echo_parameter

        Delete an echo parameter  # noqa: E501
        """
        pass

    def test_delete_rule(self):
        """Test case for delete_rule

        Delete a rule  # noqa: E501
        """
        pass

    def test_get_echo_parameter(self):
        """Test case for get_echo_parameter

        Retrieve a particular echo parameter definition  # noqa: E501
        """
        pass

    def test_get_echo_parameters(self):
        """Test case for get_echo_parameters

        Get a list of echo parameters  # noqa: E501
        """
        pass

    def test_get_rule(self):
        """Test case for get_rule

        Retrieve a particular rule definition  # noqa: E501
        """
        pass

    def test_get_rules(self):
        """Test case for get_rules

        Get a list of rules  # noqa: E501
        """
        pass

    def test_post_echo_parameter(self):
        """Test case for post_echo_parameter

        Create a new echo parameter  # noqa: E501
        """
        pass

    def test_post_rule(self):
        """Test case for post_rule

        Create a new rule  # noqa: E501
        """
        pass

    def test_put_echo_parameter(self):
        """Test case for put_echo_parameter

        Modify an echo parametr  # noqa: E501
        """
        pass

    def test_put_rule(self):
        """Test case for put_rule

        Modify a rule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
