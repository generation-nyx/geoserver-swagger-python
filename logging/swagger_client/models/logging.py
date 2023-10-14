# coding: utf-8

"""
    GeoServer Logging

    The Logging area shows logging options for the server  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Logging(object):
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
        'id': 'str',
        'level': 'str',
        'location': 'str',
        'std_out_logging': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'level': 'level',
        'location': 'location',
        'std_out_logging': 'stdOutLogging'
    }

    def __init__(self, id=None, level=None, location=None, std_out_logging=None, _configuration=None):  # noqa: E501
        """Logging - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._level = None
        self._location = None
        self._std_out_logging = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if location is not None:
            self.location = location
        if std_out_logging is not None:
            self.std_out_logging = std_out_logging

    @property
    def id(self):
        """Gets the id of this Logging.  # noqa: E501

        For internal use only. Do not modify.  # noqa: E501

        :return: The id of this Logging.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Logging.

        For internal use only. Do not modify.  # noqa: E501

        :param id: The id of this Logging.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def level(self):
        """Gets the level of this Logging.  # noqa: E501

        Logging level of GeoServer such as DEFAULT_LOGGING  # noqa: E501

        :return: The level of this Logging.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Logging.

        Logging level of GeoServer such as DEFAULT_LOGGING  # noqa: E501

        :param level: The level of this Logging.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def location(self):
        """Gets the location of this Logging.  # noqa: E501

        Logging file path. Relative to the GeoServer data directory.  # noqa: E501

        :return: The location of this Logging.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Logging.

        Logging file path. Relative to the GeoServer data directory.  # noqa: E501

        :param location: The location of this Logging.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def std_out_logging(self):
        """Gets the std_out_logging of this Logging.  # noqa: E501

        Enables/disables stdOutLogging  # noqa: E501

        :return: The std_out_logging of this Logging.  # noqa: E501
        :rtype: bool
        """
        return self._std_out_logging

    @std_out_logging.setter
    def std_out_logging(self, std_out_logging):
        """Sets the std_out_logging of this Logging.

        Enables/disables stdOutLogging  # noqa: E501

        :param std_out_logging: The std_out_logging of this Logging.  # noqa: E501
        :type: bool
        """

        self._std_out_logging = std_out_logging

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
        if issubclass(Logging, dict):
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
        if not isinstance(other, Logging):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Logging):
            return True

        return self.to_dict() != other.to_dict()