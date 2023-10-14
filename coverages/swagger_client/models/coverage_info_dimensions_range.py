# coding: utf-8

"""
    GeoServer Coverages

    A coverage is a raster data set which originates from a coverage store.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class CoverageInfoDimensionsRange(object):
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
        'max': 'float',
        'min': 'float'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, max=None, min=None, _configuration=None):  # noqa: E501
        """CoverageInfoDimensionsRange - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max = None
        self._min = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def max(self):
        """Gets the max of this CoverageInfoDimensionsRange.  # noqa: E501

        max range value  # noqa: E501

        :return: The max of this CoverageInfoDimensionsRange.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this CoverageInfoDimensionsRange.

        max range value  # noqa: E501

        :param max: The max of this CoverageInfoDimensionsRange.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this CoverageInfoDimensionsRange.  # noqa: E501

        min range value  # noqa: E501

        :return: The min of this CoverageInfoDimensionsRange.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this CoverageInfoDimensionsRange.

        min range value  # noqa: E501

        :param min: The min of this CoverageInfoDimensionsRange.  # noqa: E501
        :type: float
        """

        self._min = min

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
        if issubclass(CoverageInfoDimensionsRange, dict):
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
        if not isinstance(other, CoverageInfoDimensionsRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoverageInfoDimensionsRange):
            return True

        return self.to_dict() != other.to_dict()