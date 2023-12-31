# coding: utf-8

"""
    GeoServer Parameter Extractor

    A parameter extractor rule allows specific request parameters as URL path fragments instead of using the query string. A echo parameter makes sure that certain URL paratemers are added to the capabilities documents backlinks.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Rule(object):
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
        'activated': 'bool',
        'position': 'int',
        'parameter': 'str',
        'transform': 'str',
        'match': 'str',
        'activation': 'str',
        'remove': 'int',
        'combine': 'str'
    }

    attribute_map = {
        'id': 'id',
        'activated': 'activated',
        'position': 'position',
        'parameter': 'parameter',
        'transform': 'transform',
        'match': 'match',
        'activation': 'activation',
        'remove': 'remove',
        'combine': 'combine'
    }

    def __init__(self, id=None, activated=None, position=None, parameter=None, transform=None, match=None, activation=None, remove=None, combine=None, _configuration=None):  # noqa: E501
        """Rule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._activated = None
        self._position = None
        self._parameter = None
        self._transform = None
        self._match = None
        self._activation = None
        self._remove = None
        self._combine = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if activated is not None:
            self.activated = activated
        if position is not None:
            self.position = position
        if parameter is not None:
            self.parameter = parameter
        if transform is not None:
            self.transform = transform
        if match is not None:
            self.match = match
        if activation is not None:
            self.activation = activation
        if remove is not None:
            self.remove = remove
        if combine is not None:
            self.combine = combine

    @property
    def id(self):
        """Gets the id of this Rule.  # noqa: E501

        identifier of the rule  # noqa: E501

        :return: The id of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rule.

        identifier of the rule  # noqa: E501

        :param id: The id of this Rule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def activated(self):
        """Gets the activated of this Rule.  # noqa: E501

        Whether or not the parameter echoing is active  # noqa: E501

        :return: The activated of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this Rule.

        Whether or not the parameter echoing is active  # noqa: E501

        :param activated: The activated of this Rule.  # noqa: E501
        :type: bool
        """

        self._activated = activated

    @property
    def position(self):
        """Gets the position of this Rule.  # noqa: E501

        The position of the URL base path element to be selected  # noqa: E501

        :return: The position of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Rule.

        The position of the URL base path element to be selected  # noqa: E501

        :param position: The position of this Rule.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def parameter(self):
        """Gets the parameter of this Rule.  # noqa: E501

        The name of the parameter produced by this rule  # noqa: E501

        :return: The parameter of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this Rule.

        The name of the parameter produced by this rule  # noqa: E501

        :param parameter: The parameter of this Rule.  # noqa: E501
        :type: str
        """

        self._parameter = parameter

    @property
    def transform(self):
        """Gets the transform of this Rule.  # noqa: E501

        Expression that defines the value of the parameter, use {PARAMETER} as a placeholder for the selected path element  # noqa: E501

        :return: The transform of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this Rule.

        Expression that defines the value of the parameter, use {PARAMETER} as a placeholder for the selected path element  # noqa: E501

        :param transform: The transform of this Rule.  # noqa: E501
        :type: str
        """

        self._transform = transform

    @property
    def match(self):
        """Gets the match of this Rule.  # noqa: E501

        Regex match expression with groups, for example ^(?:/[^/]*){3}(/([^/]+)).*$ selects the URL base path third element  # noqa: E501

        :return: The match of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this Rule.

        Regex match expression with groups, for example ^(?:/[^/]*){3}(/([^/]+)).*$ selects the URL base path third element  # noqa: E501

        :param match: The match of this Rule.  # noqa: E501
        :type: str
        """

        self._match = match

    @property
    def activation(self):
        """Gets the activation of this Rule.  # noqa: E501

        If defined this rule will only be applied to URLs that match this regex expression  # noqa: E501

        :return: The activation of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._activation

    @activation.setter
    def activation(self, activation):
        """Sets the activation of this Rule.

        If defined this rule will only be applied to URLs that match this regex expression  # noqa: E501

        :param activation: The activation of this Rule.  # noqa: E501
        :type: str
        """

        self._activation = activation

    @property
    def remove(self):
        """Gets the remove of this Rule.  # noqa: E501

        The match expression group to be removed from URL, by default 1  # noqa: E501

        :return: The remove of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """Sets the remove of this Rule.

        The match expression group to be removed from URL, by default 1  # noqa: E501

        :param remove: The remove of this Rule.  # noqa: E501
        :type: int
        """

        self._remove = remove

    @property
    def combine(self):
        """Gets the combine of this Rule.  # noqa: E501

        Defines how to combine parameter existing value ($1 existing value, $2 new value), by default the value is overridden  # noqa: E501

        :return: The combine of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._combine

    @combine.setter
    def combine(self, combine):
        """Sets the combine of this Rule.

        Defines how to combine parameter existing value ($1 existing value, $2 new value), by default the value is overridden  # noqa: E501

        :param combine: The combine of this Rule.  # noqa: E501
        :type: str
        """

        self._combine = combine

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
        if issubclass(Rule, dict):
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
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
