# coding: utf-8

"""
    GeoServer Importer Extension - Data

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The data endpoint controls uploading layer data to specific import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Directory(object):
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
        'location': 'str',
        'href': 'str',
        'charset': 'str',
        'files': 'Files'
    }

    attribute_map = {
        'type': 'type',
        'location': 'location',
        'href': 'href',
        'charset': 'charset',
        'files': 'files'
    }

    def __init__(self, type=None, location=None, href=None, charset=None, files=None, _configuration=None):  # noqa: E501
        """Directory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._location = None
        self._href = None
        self._charset = None
        self._files = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if location is not None:
            self.location = location
        if href is not None:
            self.href = href
        if charset is not None:
            self.charset = charset
        if files is not None:
            self.files = files

    @property
    def type(self):
        """Gets the type of this Directory.  # noqa: E501

        \"directory\" or \"mosaic\"  # noqa: E501

        :return: The type of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Directory.

        \"directory\" or \"mosaic\"  # noqa: E501

        :param type: The type of this Directory.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def location(self):
        """Gets the location of this Directory.  # noqa: E501

        Absolute system path to the directory  # noqa: E501

        :return: The location of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Directory.

        Absolute system path to the directory  # noqa: E501

        :param location: The location of this Directory.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def href(self):
        """Gets the href of this Directory.  # noqa: E501

        URL to the directory endpoint  # noqa: E501

        :return: The href of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Directory.

        URL to the directory endpoint  # noqa: E501

        :param href: The href of this Directory.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def charset(self):
        """Gets the charset of this Directory.  # noqa: E501

        Charset encoding of the data  # noqa: E501

        :return: The charset of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this Directory.

        Charset encoding of the data  # noqa: E501

        :param charset: The charset of this Directory.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def files(self):
        """Gets the files of this Directory.  # noqa: E501


        :return: The files of this Directory.  # noqa: E501
        :rtype: Files
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Directory.


        :param files: The files of this Directory.  # noqa: E501
        :type: Files
        """

        self._files = files

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
        if issubclass(Directory, dict):
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
        if not isinstance(other, Directory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Directory):
            return True

        return self.to_dict() != other.to_dict()
