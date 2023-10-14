# coding: utf-8

"""
    GeoServer Security

    The Security area shows access rules and other configuration for the security subsystem  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class MasterPW(object):
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
        'old_master_password': 'str'
    }

    attribute_map = {
        'old_master_password': 'oldMasterPassword'
    }

    def __init__(self, old_master_password=None, _configuration=None):  # noqa: E501
        """MasterPW - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._old_master_password = None
        self.discriminator = None

        if old_master_password is not None:
            self.old_master_password = old_master_password

    @property
    def old_master_password(self):
        """Gets the old_master_password of this MasterPW.  # noqa: E501

        Current keystore password  # noqa: E501

        :return: The old_master_password of this MasterPW.  # noqa: E501
        :rtype: str
        """
        return self._old_master_password

    @old_master_password.setter
    def old_master_password(self, old_master_password):
        """Sets the old_master_password of this MasterPW.

        Current keystore password  # noqa: E501

        :param old_master_password: The old_master_password of this MasterPW.  # noqa: E501
        :type: str
        """

        self._old_master_password = old_master_password

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
        if issubclass(MasterPW, dict):
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
        if not isinstance(other, MasterPW):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MasterPW):
            return True

        return self.to_dict() != other.to_dict()
