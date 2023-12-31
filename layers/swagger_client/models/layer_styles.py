# coding: utf-8

"""
    GeoServer Layers

    A layer is a published resource (feature type or coverage).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class LayerStyles(object):
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
        '_class': 'str',
        'style': 'list[StyleReference]'
    }

    attribute_map = {
        '_class': '@class',
        'style': 'style'
    }

    def __init__(self, _class=None, style=None, _configuration=None):  # noqa: E501
        """LayerStyles - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__class = None
        self._style = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        if style is not None:
            self.style = style

    @property
    def _class(self):
        """Gets the _class of this LayerStyles.  # noqa: E501

        required value linked-hash-set.  # noqa: E501

        :return: The _class of this LayerStyles.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this LayerStyles.

        required value linked-hash-set.  # noqa: E501

        :param _class: The _class of this LayerStyles.  # noqa: E501
        :type: str
        """
        allowed_values = ["linked-hash-set"]  # noqa: E501
        if (self._configuration.client_side_validation and
                _class not in allowed_values):
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def style(self):
        """Gets the style of this LayerStyles.  # noqa: E501


        :return: The style of this LayerStyles.  # noqa: E501
        :rtype: list[StyleReference]
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this LayerStyles.


        :param style: The style of this LayerStyles.  # noqa: E501
        :type: list[StyleReference]
        """

        self._style = style

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
        if issubclass(LayerStyles, dict):
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
        if not isinstance(other, LayerStyles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LayerStyles):
            return True

        return self.to_dict() != other.to_dict()
