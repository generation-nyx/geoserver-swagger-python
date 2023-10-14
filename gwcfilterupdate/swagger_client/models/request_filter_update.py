# coding: utf-8

"""
    GeoWebCache Filter Update

    The REST API for Updating GWC filter  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RequestFilterUpdate(object):
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
        'grid_set': 'str',
        'zoom_start': 'int',
        'zoom_stop': 'int'
    }

    attribute_map = {
        'grid_set': 'gridSet',
        'zoom_start': 'zoomStart',
        'zoom_stop': 'zoomStop'
    }

    def __init__(self, grid_set=None, zoom_start=None, zoom_stop=None, _configuration=None):  # noqa: E501
        """RequestFilterUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._grid_set = None
        self._zoom_start = None
        self._zoom_stop = None
        self.discriminator = None

        if grid_set is not None:
            self.grid_set = grid_set
        if zoom_start is not None:
            self.zoom_start = zoom_start
        if zoom_stop is not None:
            self.zoom_stop = zoom_stop

    @property
    def grid_set(self):
        """Gets the grid_set of this RequestFilterUpdate.  # noqa: E501

        The projection used in the request filter.  # noqa: E501

        :return: The grid_set of this RequestFilterUpdate.  # noqa: E501
        :rtype: str
        """
        return self._grid_set

    @grid_set.setter
    def grid_set(self, grid_set):
        """Sets the grid_set of this RequestFilterUpdate.

        The projection used in the request filter.  # noqa: E501

        :param grid_set: The grid_set of this RequestFilterUpdate.  # noqa: E501
        :type: str
        """

        self._grid_set = grid_set

    @property
    def zoom_start(self):
        """Gets the zoom_start of this RequestFilterUpdate.  # noqa: E501

        This is the minimum zoom level for which the filter is applied.  # noqa: E501

        :return: The zoom_start of this RequestFilterUpdate.  # noqa: E501
        :rtype: int
        """
        return self._zoom_start

    @zoom_start.setter
    def zoom_start(self, zoom_start):
        """Sets the zoom_start of this RequestFilterUpdate.

        This is the minimum zoom level for which the filter is applied.  # noqa: E501

        :param zoom_start: The zoom_start of this RequestFilterUpdate.  # noqa: E501
        :type: int
        """

        self._zoom_start = zoom_start

    @property
    def zoom_stop(self):
        """Gets the zoom_stop of this RequestFilterUpdate.  # noqa: E501

        The maximum zoom level for which the filter is applied.  # noqa: E501

        :return: The zoom_stop of this RequestFilterUpdate.  # noqa: E501
        :rtype: int
        """
        return self._zoom_stop

    @zoom_stop.setter
    def zoom_stop(self, zoom_stop):
        """Sets the zoom_stop of this RequestFilterUpdate.

        The maximum zoom level for which the filter is applied.  # noqa: E501

        :param zoom_stop: The zoom_stop of this RequestFilterUpdate.  # noqa: E501
        :type: int
        """

        self._zoom_stop = zoom_stop

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
        if issubclass(RequestFilterUpdate, dict):
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
        if not isinstance(other, RequestFilterUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestFilterUpdate):
            return True

        return self.to_dict() != other.to_dict()