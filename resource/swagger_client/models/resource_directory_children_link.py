# coding: utf-8

"""
    GeoServer Resources

    A resource is any item in the data directory that does not represent configuration. Typical resources include styles and icons.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ResourceDirectoryChildrenLink(object):
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
        'href': 'str',
        'rel': 'str',
        'type': 'str'
    }

    attribute_map = {
        'href': 'href',
        'rel': 'rel',
        'type': 'type'
    }

    def __init__(self, href=None, rel=None, type=None, _configuration=None):  # noqa: E501
        """ResourceDirectoryChildrenLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._href = None
        self._rel = None
        self._type = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel
        if type is not None:
            self.type = type

    @property
    def href(self):
        """Gets the href of this ResourceDirectoryChildrenLink.  # noqa: E501

        The link to the resource  # noqa: E501

        :return: The href of this ResourceDirectoryChildrenLink.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ResourceDirectoryChildrenLink.

        The link to the resource  # noqa: E501

        :param href: The href of this ResourceDirectoryChildrenLink.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def rel(self):
        """Gets the rel of this ResourceDirectoryChildrenLink.  # noqa: E501

        Relationship between the current resource and the linked resource  # noqa: E501

        :return: The rel of this ResourceDirectoryChildrenLink.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this ResourceDirectoryChildrenLink.

        Relationship between the current resource and the linked resource  # noqa: E501

        :param rel: The rel of this ResourceDirectoryChildrenLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["alternate"]  # noqa: E501
        if (self._configuration.client_side_validation and
                rel not in allowed_values):
            raise ValueError(
                "Invalid value for `rel` ({0}), must be one of {1}"  # noqa: E501
                .format(rel, allowed_values)
            )

        self._rel = rel

    @property
    def type(self):
        """Gets the type of this ResourceDirectoryChildrenLink.  # noqa: E501

        The mime type returned by the link  # noqa: E501

        :return: The type of this ResourceDirectoryChildrenLink.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceDirectoryChildrenLink.

        The mime type returned by the link  # noqa: E501

        :param type: The type of this ResourceDirectoryChildrenLink.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ResourceDirectoryChildrenLink, dict):
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
        if not isinstance(other, ResourceDirectoryChildrenLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceDirectoryChildrenLink):
            return True

        return self.to_dict() != other.to_dict()
