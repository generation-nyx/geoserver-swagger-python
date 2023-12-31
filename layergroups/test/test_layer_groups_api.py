# coding: utf-8

"""
    GeoServer Layer Groups

    A layer group is a group of layers that can be referenced as a single layer as part of a WMS request. A layer group can also be used as a container for layers.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.layer_groups_api import LayerGroupsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLayerGroupsApi(unittest.TestCase):
    """LayerGroupsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.layer_groups_api.LayerGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_layergroup(self):
        """Test case for delete_layergroup

        Delete layer group  # noqa: E501
        """
        pass

    def test_delete_layergroups(self):
        """Test case for delete_layergroups

        """
        pass

    def test_delete_workspace_layergroup(self):
        """Test case for delete_workspace_layergroup

        Delete layer group  # noqa: E501
        """
        pass

    def test_delete_workspace_layergroups(self):
        """Test case for delete_workspace_layergroups

        """
        pass

    def test_get_layergroup(self):
        """Test case for get_layergroup

        Retrieve a layer group  # noqa: E501
        """
        pass

    def test_get_layergroups(self):
        """Test case for get_layergroups

        Get a list of layer groups  # noqa: E501
        """
        pass

    def test_get_workspace_layergroup(self):
        """Test case for get_workspace_layergroup

        Retrieve a layer group  # noqa: E501
        """
        pass

    def test_get_workspace_layergroups(self):
        """Test case for get_workspace_layergroups

        Get a list of layer groups in a workspace  # noqa: E501
        """
        pass

    def test_post_layergroup(self):
        """Test case for post_layergroup

        """
        pass

    def test_post_layergroups(self):
        """Test case for post_layergroups

        Add a new layer group  # noqa: E501
        """
        pass

    def test_post_workspace_layergroup(self):
        """Test case for post_workspace_layergroup

        """
        pass

    def test_post_workspace_layergroups(self):
        """Test case for post_workspace_layergroups

        Add a new layer group  # noqa: E501
        """
        pass

    def test_put_layergroup(self):
        """Test case for put_layergroup

        Modify a layer group.  # noqa: E501
        """
        pass

    def test_put_layergroups(self):
        """Test case for put_layergroups

        """
        pass

    def test_put_workspace_layergroup(self):
        """Test case for put_workspace_layergroup

        Modify a layer group.  # noqa: E501
        """
        pass

    def test_put_workspace_layergroups(self):
        """Test case for put_workspace_layergroups

        """
        pass


if __name__ == '__main__':
    unittest.main()
