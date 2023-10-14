# coding: utf-8

"""
    GeoServer Feature Types

    A feature type is a vector based spatial resource or data set that originates from a data store. In some cases, such as with a shapefile, a feature type has a one-to-one relationship with its data store. In other cases, such as PostGIS, the relationship of feature type to data store is many-to-one, feature types corresponding to a table in the database.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.feature_type_info_keywords import FeatureTypeInfoKeywords  # noqa: E501
from swagger_client.rest import ApiException


class TestFeatureTypeInfoKeywords(unittest.TestCase):
    """FeatureTypeInfoKeywords unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFeatureTypeInfoKeywords(self):
        """Test FeatureTypeInfoKeywords"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.feature_type_info_keywords.FeatureTypeInfoKeywords()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
