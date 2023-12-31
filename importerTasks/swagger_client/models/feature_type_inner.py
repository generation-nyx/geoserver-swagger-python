# coding: utf-8

"""
    GeoServer Importer Extension - Tasks

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The tasks endpoint controls individual tasks within an import job. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class FeatureTypeInner(object):
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
        'binding': 'str'
    }

    attribute_map = {
        'name': 'name',
        'binding': 'binding'
    }

    def __init__(self, name=None, binding=None, _configuration=None):  # noqa: E501
        """FeatureTypeInner - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._binding = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if binding is not None:
            self.binding = binding

    @property
    def name(self):
        """Gets the name of this FeatureTypeInner.  # noqa: E501

        The name of the attribute  # noqa: E501

        :return: The name of this FeatureTypeInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureTypeInner.

        The name of the attribute  # noqa: E501

        :param name: The name of this FeatureTypeInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def binding(self):
        """Gets the binding of this FeatureTypeInner.  # noqa: E501

        The java class representing the type of the attribute  # noqa: E501

        :return: The binding of this FeatureTypeInner.  # noqa: E501
        :rtype: str
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this FeatureTypeInner.

        The java class representing the type of the attribute  # noqa: E501

        :param binding: The binding of this FeatureTypeInner.  # noqa: E501
        :type: str
        """

        self._binding = binding

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
        if issubclass(FeatureTypeInner, dict):
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
        if not isinstance(other, FeatureTypeInner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureTypeInner):
            return True

        return self.to_dict() != other.to_dict()
