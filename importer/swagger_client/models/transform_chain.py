# coding: utf-8

"""
    GeoServer Importer Extension - Main

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The main endpoint manages individual import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class TransformChain(object):
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
        'transforms': 'Transforms'
    }

    attribute_map = {
        'type': 'type',
        'transforms': 'transforms'
    }

    def __init__(self, type=None, transforms=None, _configuration=None):  # noqa: E501
        """TransformChain - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._transforms = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if transforms is not None:
            self.transforms = transforms

    @property
    def type(self):
        """Gets the type of this TransformChain.  # noqa: E501

        The type of transforms in the chain. One of \"vector\" or \"raster\"  # noqa: E501

        :return: The type of this TransformChain.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransformChain.

        The type of transforms in the chain. One of \"vector\" or \"raster\"  # noqa: E501

        :param type: The type of this TransformChain.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def transforms(self):
        """Gets the transforms of this TransformChain.  # noqa: E501


        :return: The transforms of this TransformChain.  # noqa: E501
        :rtype: Transforms
        """
        return self._transforms

    @transforms.setter
    def transforms(self, transforms):
        """Sets the transforms of this TransformChain.


        :param transforms: The transforms of this TransformChain.  # noqa: E501
        :type: Transforms
        """

        self._transforms = transforms

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
        if issubclass(TransformChain, dict):
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
        if not isinstance(other, TransformChain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransformChain):
            return True

        return self.to_dict() != other.to_dict()
