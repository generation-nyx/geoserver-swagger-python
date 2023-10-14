# coding: utf-8

# flake8: noqa

"""
    GeoServer Data Stores

    A data store contains vector format spatial data. It can be a file (such as a shapefile), a database (such as PostGIS), or a server (such as a remote Web Feature Service).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.data_stores_api import DataStoresApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.data_store_response import DataStoreResponse
from swagger_client.models.datastore import Datastore
from swagger_client.models.datastore1 import Datastore1
from swagger_client.models.entry import Entry
from swagger_client.models.workspace import Workspace
