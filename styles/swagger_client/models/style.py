# coding: utf-8

"""
    GeoServer Styles

    A style describes how a resource is symbolized or rendered by the Web Map Service.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Style(object):
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
        'name': 'str',
        'format': 'str',
        'language_version': 'StyleLanguageVersion',
        'filename': 'str'
    }

    attribute_map = {
        'name': 'name',
        'format': 'format',
        'language_version': 'languageVersion',
        'filename': 'filename'
    }

    def __init__(self, name=None, format=None, language_version=None, filename=None, _configuration=None):  # noqa: E501
        """Style - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._format = None
        self._language_version = None
        self._filename = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if format is not None:
            self.format = format
        if language_version is not None:
            self.language_version = language_version
        if filename is not None:
            self.filename = filename

    @property
    def name(self):
        """Gets the name of this Style.  # noqa: E501

        Name of style  # noqa: E501

        :return: The name of this Style.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Style.

        Name of style  # noqa: E501

        :param name: The name of this Style.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def format(self):
        """Gets the format of this Style.  # noqa: E501

        Format of style  # noqa: E501

        :return: The format of this Style.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Style.

        Format of style  # noqa: E501

        :param format: The format of this Style.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def language_version(self):
        """Gets the language_version of this Style.  # noqa: E501


        :return: The language_version of this Style.  # noqa: E501
        :rtype: StyleLanguageVersion
        """
        return self._language_version

    @language_version.setter
    def language_version(self, language_version):
        """Sets the language_version of this Style.


        :param language_version: The language_version of this Style.  # noqa: E501
        :type: StyleLanguageVersion
        """

        self._language_version = language_version

    @property
    def filename(self):
        """Gets the filename of this Style.  # noqa: E501

        File name of the style  # noqa: E501

        :return: The filename of this Style.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Style.

        File name of the style  # noqa: E501

        :param filename: The filename of this Style.  # noqa: E501
        :type: str
        """

        self._filename = filename

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
        if issubclass(Style, dict):
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
        if not isinstance(other, Style):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Style):
            return True

        return self.to_dict() != other.to_dict()
