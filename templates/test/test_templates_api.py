# coding: utf-8

"""
    GeoServer Template

    Manage templates used to configure output (for example GetFeatureInfo reponse). Templates can be registered for the entire server or workspace. You can also configure a template for use with a store, featureType or coverage.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.templates_api import TemplatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.templates_api.TemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_template_coverage_delete(self):
        """Test case for template_coverage_delete

        Delete a template.  # noqa: E501
        """
        pass

    def test_template_coverage_get(self):
        """Test case for template_coverage_get

        Return a template for a coverage  # noqa: E501
        """
        pass

    def test_template_coverage_post(self):
        """Test case for template_coverage_post

        """
        pass

    def test_template_coverage_put(self):
        """Test case for template_coverage_put

        Insert or update a template  # noqa: E501
        """
        pass

    def test_template_data_store_cs_delete(self):
        """Test case for template_data_store_cs_delete

        Delete a template.  # noqa: E501
        """
        pass

    def test_template_data_store_cs_get(self):
        """Test case for template_data_store_cs_get

        Return a template for a coverage store  # noqa: E501
        """
        pass

    def test_template_data_store_cs_post(self):
        """Test case for template_data_store_cs_post

        """
        pass

    def test_template_data_store_cs_put(self):
        """Test case for template_data_store_cs_put

        Insert or update a template  # noqa: E501
        """
        pass

    def test_template_data_store_delete(self):
        """Test case for template_data_store_delete

        Delete a template.  # noqa: E501
        """
        pass

    def test_template_data_store_ft_delete(self):
        """Test case for template_data_store_ft_delete

        Delete a template.  # noqa: E501
        """
        pass

    def test_template_data_store_ft_get(self):
        """Test case for template_data_store_ft_get

        Return a template for a feature type.  # noqa: E501
        """
        pass

    def test_template_data_store_ft_post(self):
        """Test case for template_data_store_ft_post

        """
        pass

    def test_template_data_store_ft_put(self):
        """Test case for template_data_store_ft_put

        Insert or update a template  # noqa: E501
        """
        pass

    def test_template_data_store_get(self):
        """Test case for template_data_store_get

        Return a template for a data store  # noqa: E501
        """
        pass

    def test_template_data_store_post(self):
        """Test case for template_data_store_post

        """
        pass

    def test_template_data_store_put(self):
        """Test case for template_data_store_put

        Insert or update a template  # noqa: E501
        """
        pass

    def test_template_delete(self):
        """Test case for template_delete

        Delete a template.  # noqa: E501
        """
        pass

    def test_template_get(self):
        """Test case for template_get

        Return a template  # noqa: E501
        """
        pass

    def test_template_post(self):
        """Test case for template_post

        """
        pass

    def test_template_put(self):
        """Test case for template_put

        Insert or update a template  # noqa: E501
        """
        pass

    def test_template_workspace_delete(self):
        """Test case for template_workspace_delete

        Delete a template.  # noqa: E501
        """
        pass

    def test_template_workspace_get(self):
        """Test case for template_workspace_get

        Return a template for workspace  # noqa: E501
        """
        pass

    def test_template_workspace_post(self):
        """Test case for template_workspace_post

        """
        pass

    def test_template_workspace_put(self):
        """Test case for template_workspace_put

        Insert or update a template  # noqa: E501
        """
        pass

    def test_templates_coverage_delete(self):
        """Test case for templates_coverage_delete

        """
        pass

    def test_templates_coverage_get(self):
        """Test case for templates_coverage_get

        List of templates for a coverage  # noqa: E501
        """
        pass

    def test_templates_coverage_post(self):
        """Test case for templates_coverage_post

        """
        pass

    def test_templates_coverage_put(self):
        """Test case for templates_coverage_put

        """
        pass

    def test_templates_data_store_cs_delete(self):
        """Test case for templates_data_store_cs_delete

        """
        pass

    def test_templates_data_store_cs_get(self):
        """Test case for templates_data_store_cs_get

        List of templates for a coverage store  # noqa: E501
        """
        pass

    def test_templates_data_store_cs_post(self):
        """Test case for templates_data_store_cs_post

        """
        pass

    def test_templates_data_store_cs_put(self):
        """Test case for templates_data_store_cs_put

        """
        pass

    def test_templates_data_store_delete(self):
        """Test case for templates_data_store_delete

        """
        pass

    def test_templates_data_store_ft_delete(self):
        """Test case for templates_data_store_ft_delete

        """
        pass

    def test_templates_data_store_ft_get(self):
        """Test case for templates_data_store_ft_get

        List of templates for a feature type.  # noqa: E501
        """
        pass

    def test_templates_data_store_ft_post(self):
        """Test case for templates_data_store_ft_post

        """
        pass

    def test_templates_data_store_ft_put(self):
        """Test case for templates_data_store_ft_put

        """
        pass

    def test_templates_data_store_get(self):
        """Test case for templates_data_store_get

        List of templates for a data store  # noqa: E501
        """
        pass

    def test_templates_data_store_post(self):
        """Test case for templates_data_store_post

        """
        pass

    def test_templates_data_store_put(self):
        """Test case for templates_data_store_put

        """
        pass

    def test_templates_delete(self):
        """Test case for templates_delete

        """
        pass

    def test_templates_get(self):
        """Test case for templates_get

        List of templates for the server  # noqa: E501
        """
        pass

    def test_templates_post(self):
        """Test case for templates_post

        """
        pass

    def test_templates_put(self):
        """Test case for templates_put

        """
        pass

    def test_templates_workspace_delete(self):
        """Test case for templates_workspace_delete

        """
        pass

    def test_templates_workspace_get(self):
        """Test case for templates_workspace_get

        List of templates for workspace  # noqa: E501
        """
        pass

    def test_templates_workspace_post(self):
        """Test case for templates_workspace_post

        """
        pass

    def test_templates_workspace_put(self):
        """Test case for templates_workspace_put

        """
        pass


if __name__ == '__main__':
    unittest.main()
