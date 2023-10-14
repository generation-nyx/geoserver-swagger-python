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


class InlineResponse200(object):
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
        'coverages': 'InlineResponse200Coverages'
    }

    attribute_map = {
        'coverages': 'coverages'
    }

    def __init__(self, coverages=None, _configuration=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._coverages = None
        self.discriminator = None

        if coverages is not None:
            self.coverages = coverages

    @property
    def coverages(self):
        """Gets the coverages of this InlineResponse200.  # noqa: E501


        :return: The coverages of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200Coverages
        """
        return self._coverages

    @coverages.setter
    def coverages(self, coverages):
        """Sets the coverages of this InlineResponse200.


        :param coverages: The coverages of this InlineResponse200.  # noqa: E501
        :type: InlineResponse200Coverages
        """

        self._coverages = coverages

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse200):
            return True

        return self.to_dict() != other.to_dict()
