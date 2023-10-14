# coding: utf-8

"""
    GeoServer Data Stores

    A data store contains vector format spatial data. It can be a file (such as a shapefile), a database (such as PostGIS), or a server (such as a remote Web Feature Service).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Datastore(object):
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
        'description': 'str',
        'enabled': 'bool',
        'workspace': 'Workspace',
        'connection_parameters': 'list[Entry]',
        'default': 'bool',
        'feature_types': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'workspace': 'workspace',
        'connection_parameters': 'connectionParameters',
        'default': '__default',
        'feature_types': 'featureTypes'
    }

    def __init__(self, name=None, description=None, enabled=None, workspace=None, connection_parameters=None, default=None, feature_types=None, _configuration=None):  # noqa: E501
        """Datastore - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._enabled = None
        self._workspace = None
        self._connection_parameters = None
        self._default = None
        self._feature_types = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if workspace is not None:
            self.workspace = workspace
        if connection_parameters is not None:
            self.connection_parameters = connection_parameters
        if default is not None:
            self.default = default
        if feature_types is not None:
            self.feature_types = feature_types

    @property
    def name(self):
        """Gets the name of this Datastore.  # noqa: E501

        Name of data store  # noqa: E501

        :return: The name of this Datastore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Datastore.

        Name of data store  # noqa: E501

        :param name: The name of this Datastore.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Datastore.  # noqa: E501

        Description of data store  # noqa: E501

        :return: The description of this Datastore.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Datastore.

        Description of data store  # noqa: E501

        :param description: The description of this Datastore.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this Datastore.  # noqa: E501

        Whether or not the data store is enabled  # noqa: E501

        :return: The enabled of this Datastore.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Datastore.

        Whether or not the data store is enabled  # noqa: E501

        :param enabled: The enabled of this Datastore.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def workspace(self):
        """Gets the workspace of this Datastore.  # noqa: E501


        :return: The workspace of this Datastore.  # noqa: E501
        :rtype: Workspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this Datastore.


        :param workspace: The workspace of this Datastore.  # noqa: E501
        :type: Workspace
        """

        self._workspace = workspace

    @property
    def connection_parameters(self):
        """Gets the connection_parameters of this Datastore.  # noqa: E501


        :return: The connection_parameters of this Datastore.  # noqa: E501
        :rtype: list[Entry]
        """
        return self._connection_parameters

    @connection_parameters.setter
    def connection_parameters(self, connection_parameters):
        """Sets the connection_parameters of this Datastore.


        :param connection_parameters: The connection_parameters of this Datastore.  # noqa: E501
        :type: list[Entry]
        """

        self._connection_parameters = connection_parameters

    @property
    def default(self):
        """Gets the default of this Datastore.  # noqa: E501

        Whether or not the data store is the default data store  # noqa: E501

        :return: The default of this Datastore.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Datastore.

        Whether or not the data store is the default data store  # noqa: E501

        :param default: The default of this Datastore.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def feature_types(self):
        """Gets the feature_types of this Datastore.  # noqa: E501


        :return: The feature_types of this Datastore.  # noqa: E501
        :rtype: list[str]
        """
        return self._feature_types

    @feature_types.setter
    def feature_types(self, feature_types):
        """Sets the feature_types of this Datastore.


        :param feature_types: The feature_types of this Datastore.  # noqa: E501
        :type: list[str]
        """

        self._feature_types = feature_types

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
        if issubclass(Datastore, dict):
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
        if not isinstance(other, Datastore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Datastore):
            return True

        return self.to_dict() != other.to_dict()