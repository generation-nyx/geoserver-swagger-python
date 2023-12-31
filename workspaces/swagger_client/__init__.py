# coding: utf-8

# flake8: noqa

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.workspaces_api import WorkspacesApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.workspace import Workspace
from swagger_client.models.workspace_response import WorkspaceResponse
from swagger_client.models.workspace_workspace import WorkspaceWorkspace
from swagger_client.models.workspaces_response import WorkspacesResponse
