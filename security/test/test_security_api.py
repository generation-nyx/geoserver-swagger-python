# coding: utf-8

"""
    GeoServer Security

    The Security area shows access rules and other configuration for the security subsystem  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.security_api import SecurityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.security_api.SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_acl_layer(self):
        """Test case for delete_acl_layer

        Delete layer rule.  # noqa: E501
        """
        pass

    def test_delete_acl_layers(self):
        """Test case for delete_acl_layers

        Delete layer rule(s)  # noqa: E501
        """
        pass

    def test_delete_acl_service(self):
        """Test case for delete_acl_service

        Delete service rule.  # noqa: E501
        """
        pass

    def test_delete_acl_services(self):
        """Test case for delete_acl_services

        Delete service rule(s)  # noqa: E501
        """
        pass

    def test_delete_aclrest_rule(self):
        """Test case for delete_aclrest_rule

        Delete REST access rule  # noqa: E501
        """
        pass

    def test_delete_aclrest_rules(self):
        """Test case for delete_aclrest_rules

        Delete REST access rule(s)  # noqa: E501
        """
        pass

    def test_delete_catalog_mode(self):
        """Test case for delete_catalog_mode

        """
        pass

    def test_delete_master_pw(self):
        """Test case for delete_master_pw

        """
        pass

    def test_delete_self_password(self):
        """Test case for delete_self_password

        """
        pass

    def test_get_acl_layer(self):
        """Test case for get_acl_layer

        """
        pass

    def test_get_acl_layers(self):
        """Test case for get_acl_layers

        Get layer rules  # noqa: E501
        """
        pass

    def test_get_acl_service(self):
        """Test case for get_acl_service

        """
        pass

    def test_get_acl_services(self):
        """Test case for get_acl_services

        Get service rules  # noqa: E501
        """
        pass

    def test_get_aclrest_rule(self):
        """Test case for get_aclrest_rule

        """
        pass

    def test_get_aclrest_rules(self):
        """Test case for get_aclrest_rules

        Get REST rules  # noqa: E501
        """
        pass

    def test_get_catalog_mode(self):
        """Test case for get_catalog_mode

        """
        pass

    def test_get_master_pw(self):
        """Test case for get_master_pw

        Get keystore password  # noqa: E501
        """
        pass

    def test_get_self_password(self):
        """Test case for get_self_password

        """
        pass

    def test_post_acl_layer(self):
        """Test case for post_acl_layer

        """
        pass

    def test_post_acl_layers(self):
        """Test case for post_acl_layers

        Add layer rule(s)  # noqa: E501
        """
        pass

    def test_post_acl_service(self):
        """Test case for post_acl_service

        """
        pass

    def test_post_acl_services(self):
        """Test case for post_acl_services

        Add service rule(s)  # noqa: E501
        """
        pass

    def test_post_aclrest_rule(self):
        """Test case for post_aclrest_rule

        """
        pass

    def test_post_aclrest_rules(self):
        """Test case for post_aclrest_rules

        Add REST access rule(s)  # noqa: E501
        """
        pass

    def test_post_catalog_mode(self):
        """Test case for post_catalog_mode

        """
        pass

    def test_post_master_pw(self):
        """Test case for post_master_pw

        """
        pass

    def test_post_self_password(self):
        """Test case for post_self_password

        """
        pass

    def test_put_acl_layer(self):
        """Test case for put_acl_layer

        """
        pass

    def test_put_acl_layers(self):
        """Test case for put_acl_layers

        Edit layer rule(s)  # noqa: E501
        """
        pass

    def test_put_acl_service(self):
        """Test case for put_acl_service

        """
        pass

    def test_put_acl_services(self):
        """Test case for put_acl_services

        Edit service rule(s)  # noqa: E501
        """
        pass

    def test_put_aclrest_rule(self):
        """Test case for put_aclrest_rule

        """
        pass

    def test_put_aclrest_rules(self):
        """Test case for put_aclrest_rules

        Edit REST access rule(s)  # noqa: E501
        """
        pass

    def test_put_master_pw(self):
        """Test case for put_master_pw

        Update keystore password  # noqa: E501
        """
        pass

    def test_put_self_password(self):
        """Test case for put_self_password

        Update password  # noqa: E501
        """
        pass

    def test_rest_security_acl_catalog_put(self):
        """Test case for rest_security_acl_catalog_put

        Update catalog mode  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
