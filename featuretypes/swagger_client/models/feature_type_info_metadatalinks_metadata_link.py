# coding: utf-8

"""
    GeoServer Feature Types

    A feature type is a vector based spatial resource or data set that originates from a data store. In some cases, such as with a shapefile, a feature type has a one-to-one relationship with its data store. In other cases, such as PostGIS, the relationship of feature type to data store is many-to-one, feature types corresponding to a table in the database.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class FeatureTypeInfoMetadatalinksMetadataLink(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'metadata_type': 'str',
        'content': 'str'
    }

    attribute_map = {
        'type': 'type',
        'metadata_type': 'metadataType',
        'content': 'content'
    }

    def __init__(self, type=None, metadata_type=None, content=None, _configuration=None):  # noqa: E501
        """FeatureTypeInfoMetadatalinksMetadataLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._metadata_type = None
        self._content = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if metadata_type is not None:
            self.metadata_type = metadata_type
        if content is not None:
            self.content = content

    @property
    def type(self):
        """Gets the type of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501

        The MIME type  # noqa: E501

        :return: The type of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeatureTypeInfoMetadatalinksMetadataLink.

        The MIME type  # noqa: E501

        :param type: The type of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def metadata_type(self):
        """Gets the metadata_type of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501

        The type of metadata, e.g. \"FGDC\"  # noqa: E501

        :return: The metadata_type of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501
        :rtype: str
        """
        return self._metadata_type

    @metadata_type.setter
    def metadata_type(self, metadata_type):
        """Sets the metadata_type of this FeatureTypeInfoMetadatalinksMetadataLink.

        The type of metadata, e.g. \"FGDC\"  # noqa: E501

        :param metadata_type: The metadata_type of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501
        :type: str
        """

        self._metadata_type = metadata_type

    @property
    def content(self):
        """Gets the content of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501

        The link URL  # noqa: E501

        :return: The content of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this FeatureTypeInfoMetadatalinksMetadataLink.

        The link URL  # noqa: E501

        :param content: The content of this FeatureTypeInfoMetadatalinksMetadataLink.  # noqa: E501
        :type: str
        """

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FeatureTypeInfoMetadatalinksMetadataLink, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeatureTypeInfoMetadatalinksMetadataLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureTypeInfoMetadatalinksMetadataLink):
            return True

        return self.to_dict() != other.to_dict()
