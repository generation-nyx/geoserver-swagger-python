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


class LayerAttribution(object):
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
        'title': 'str',
        'href': 'str',
        'logo_url': 'str',
        'logo_width': 'int',
        'logo_height': 'int',
        'logo_type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'href': 'href',
        'logo_url': 'logoURL',
        'logo_width': 'logoWidth',
        'logo_height': 'logoHeight',
        'logo_type': 'logoType'
    }

    def __init__(self, title=None, href=None, logo_url=None, logo_width=None, logo_height=None, logo_type=None, _configuration=None):  # noqa: E501
        """LayerAttribution - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._title = None
        self._href = None
        self._logo_url = None
        self._logo_width = None
        self._logo_height = None
        self._logo_type = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if href is not None:
            self.href = href
        if logo_url is not None:
            self.logo_url = logo_url
        if logo_width is not None:
            self.logo_width = logo_width
        if logo_height is not None:
            self.logo_height = logo_height
        if logo_type is not None:
            self.logo_type = logo_type

    @property
    def title(self):
        """Gets the title of this LayerAttribution.  # noqa: E501

        Human-readable text describing the data provider  # noqa: E501

        :return: The title of this LayerAttribution.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LayerAttribution.

        Human-readable text describing the data provider  # noqa: E501

        :param title: The title of this LayerAttribution.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def href(self):
        """Gets the href of this LayerAttribution.  # noqa: E501

        URL to data provider  # noqa: E501

        :return: The href of this LayerAttribution.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LayerAttribution.

        URL to data provider  # noqa: E501

        :param href: The href of this LayerAttribution.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def logo_url(self):
        """Gets the logo_url of this LayerAttribution.  # noqa: E501

        Data provider logo  # noqa: E501

        :return: The logo_url of this LayerAttribution.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this LayerAttribution.

        Data provider logo  # noqa: E501

        :param logo_url: The logo_url of this LayerAttribution.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def logo_width(self):
        """Gets the logo_width of this LayerAttribution.  # noqa: E501

        Data provider logo width  # noqa: E501

        :return: The logo_width of this LayerAttribution.  # noqa: E501
        :rtype: int
        """
        return self._logo_width

    @logo_width.setter
    def logo_width(self, logo_width):
        """Sets the logo_width of this LayerAttribution.

        Data provider logo width  # noqa: E501

        :param logo_width: The logo_width of this LayerAttribution.  # noqa: E501
        :type: int
        """

        self._logo_width = logo_width

    @property
    def logo_height(self):
        """Gets the logo_height of this LayerAttribution.  # noqa: E501

        Data provider logo height  # noqa: E501

        :return: The logo_height of this LayerAttribution.  # noqa: E501
        :rtype: int
        """
        return self._logo_height

    @logo_height.setter
    def logo_height(self, logo_height):
        """Sets the logo_height of this LayerAttribution.

        Data provider logo height  # noqa: E501

        :param logo_height: The logo_height of this LayerAttribution.  # noqa: E501
        :type: int
        """

        self._logo_height = logo_height

    @property
    def logo_type(self):
        """Gets the logo_type of this LayerAttribution.  # noqa: E501

        Format of data provider logo, example \"image/png\"  # noqa: E501

        :return: The logo_type of this LayerAttribution.  # noqa: E501
        :rtype: str
        """
        return self._logo_type

    @logo_type.setter
    def logo_type(self, logo_type):
        """Sets the logo_type of this LayerAttribution.

        Format of data provider logo, example \"image/png\"  # noqa: E501

        :param logo_type: The logo_type of this LayerAttribution.  # noqa: E501
        :type: str
        """

        self._logo_type = logo_type

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
        if issubclass(LayerAttribution, dict):
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
        if not isinstance(other, LayerAttribution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LayerAttribution):
            return True

        return self.to_dict() != other.to_dict()