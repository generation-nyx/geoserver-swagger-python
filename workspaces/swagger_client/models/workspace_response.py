# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WorkspaceResponse(object):
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
        'data_stores': 'str',
        'coverage_stores': 'str',
        'wms_stores': 'str'
    }

    attribute_map = {
        'name': 'name',
        'data_stores': 'dataStores',
        'coverage_stores': 'coverageStores',
        'wms_stores': 'wmsStores'
    }

    def __init__(self, name=None, data_stores=None, coverage_stores=None, wms_stores=None, _configuration=None):  # noqa: E501
        """WorkspaceResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._data_stores = None
        self._coverage_stores = None
        self._wms_stores = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if data_stores is not None:
            self.data_stores = data_stores
        if coverage_stores is not None:
            self.coverage_stores = coverage_stores
        if wms_stores is not None:
            self.wms_stores = wms_stores

    @property
    def name(self):
        """Gets the name of this WorkspaceResponse.  # noqa: E501

        Name of workspace  # noqa: E501

        :return: The name of this WorkspaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceResponse.

        Name of workspace  # noqa: E501

        :param name: The name of this WorkspaceResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_stores(self):
        """Gets the data_stores of this WorkspaceResponse.  # noqa: E501

        URL to Datas tores in this workspace  # noqa: E501

        :return: The data_stores of this WorkspaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_stores

    @data_stores.setter
    def data_stores(self, data_stores):
        """Sets the data_stores of this WorkspaceResponse.

        URL to Datas tores in this workspace  # noqa: E501

        :param data_stores: The data_stores of this WorkspaceResponse.  # noqa: E501
        :type: str
        """

        self._data_stores = data_stores

    @property
    def coverage_stores(self):
        """Gets the coverage_stores of this WorkspaceResponse.  # noqa: E501

        URL to Coverage stores in this workspace  # noqa: E501

        :return: The coverage_stores of this WorkspaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._coverage_stores

    @coverage_stores.setter
    def coverage_stores(self, coverage_stores):
        """Sets the coverage_stores of this WorkspaceResponse.

        URL to Coverage stores in this workspace  # noqa: E501

        :param coverage_stores: The coverage_stores of this WorkspaceResponse.  # noqa: E501
        :type: str
        """

        self._coverage_stores = coverage_stores

    @property
    def wms_stores(self):
        """Gets the wms_stores of this WorkspaceResponse.  # noqa: E501

        URL to WMS stores in this workspace  # noqa: E501

        :return: The wms_stores of this WorkspaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._wms_stores

    @wms_stores.setter
    def wms_stores(self, wms_stores):
        """Sets the wms_stores of this WorkspaceResponse.

        URL to WMS stores in this workspace  # noqa: E501

        :param wms_stores: The wms_stores of this WorkspaceResponse.  # noqa: E501
        :type: str
        """

        self._wms_stores = wms_stores

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
        if issubclass(WorkspaceResponse, dict):
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
        if not isinstance(other, WorkspaceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceResponse):
            return True

        return self.to_dict() != other.to_dict()
