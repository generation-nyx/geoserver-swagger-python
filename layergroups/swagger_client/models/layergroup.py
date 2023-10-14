# coding: utf-8

"""
    GeoServer Layer Groups

    A layer group is a group of layers that can be referenced as a single layer as part of a WMS request. A layer group can also be used as a container for layers.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Layergroup(object):
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
        'mode': 'str',
        'title': 'str',
        'abstract_txt': 'str',
        'workspace': 'LayergroupWorkspace',
        'publishables': 'LayergroupPublishables',
        'styles': 'LayergroupStyles',
        'metadata_links': 'list[LayergroupMetadataLink]',
        'bounds': 'LayergroupBounds',
        'keywords': 'LayergroupKeywords'
    }

    attribute_map = {
        'name': 'name',
        'mode': 'mode',
        'title': 'title',
        'abstract_txt': 'abstractTxt',
        'workspace': 'workspace',
        'publishables': 'publishables',
        'styles': 'styles',
        'metadata_links': 'metadataLinks',
        'bounds': 'bounds',
        'keywords': 'keywords'
    }

    def __init__(self, name=None, mode=None, title=None, abstract_txt=None, workspace=None, publishables=None, styles=None, metadata_links=None, bounds=None, keywords=None, _configuration=None):  # noqa: E501
        """Layergroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._mode = None
        self._title = None
        self._abstract_txt = None
        self._workspace = None
        self._publishables = None
        self._styles = None
        self._metadata_links = None
        self._bounds = None
        self._keywords = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if title is not None:
            self.title = title
        if abstract_txt is not None:
            self.abstract_txt = abstract_txt
        if workspace is not None:
            self.workspace = workspace
        if publishables is not None:
            self.publishables = publishables
        if styles is not None:
            self.styles = styles
        if metadata_links is not None:
            self.metadata_links = metadata_links
        if bounds is not None:
            self.bounds = bounds
        if keywords is not None:
            self.keywords = keywords

    @property
    def name(self):
        """Gets the name of this Layergroup.  # noqa: E501

        Name of the layer group  # noqa: E501

        :return: The name of this Layergroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Layergroup.

        Name of the layer group  # noqa: E501

        :param name: The name of this Layergroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mode(self):
        """Gets the mode of this Layergroup.  # noqa: E501

        Name of the layer group mode. Can be SINGLE, NAMED, CONTAINER, or EO.  # noqa: E501

        :return: The mode of this Layergroup.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Layergroup.

        Name of the layer group mode. Can be SINGLE, NAMED, CONTAINER, or EO.  # noqa: E501

        :param mode: The mode of this Layergroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["SINGLE", "NAMED", "CONTAINER", "EO"]  # noqa: E501
        if (self._configuration.client_side_validation and
                mode not in allowed_values):
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def title(self):
        """Gets the title of this Layergroup.  # noqa: E501

        Title of the layer group  # noqa: E501

        :return: The title of this Layergroup.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Layergroup.

        Title of the layer group  # noqa: E501

        :param title: The title of this Layergroup.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def abstract_txt(self):
        """Gets the abstract_txt of this Layergroup.  # noqa: E501

        Abstract of the layer group  # noqa: E501

        :return: The abstract_txt of this Layergroup.  # noqa: E501
        :rtype: str
        """
        return self._abstract_txt

    @abstract_txt.setter
    def abstract_txt(self, abstract_txt):
        """Sets the abstract_txt of this Layergroup.

        Abstract of the layer group  # noqa: E501

        :param abstract_txt: The abstract_txt of this Layergroup.  # noqa: E501
        :type: str
        """

        self._abstract_txt = abstract_txt

    @property
    def workspace(self):
        """Gets the workspace of this Layergroup.  # noqa: E501


        :return: The workspace of this Layergroup.  # noqa: E501
        :rtype: LayergroupWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this Layergroup.


        :param workspace: The workspace of this Layergroup.  # noqa: E501
        :type: LayergroupWorkspace
        """

        self._workspace = workspace

    @property
    def publishables(self):
        """Gets the publishables of this Layergroup.  # noqa: E501


        :return: The publishables of this Layergroup.  # noqa: E501
        :rtype: LayergroupPublishables
        """
        return self._publishables

    @publishables.setter
    def publishables(self, publishables):
        """Sets the publishables of this Layergroup.


        :param publishables: The publishables of this Layergroup.  # noqa: E501
        :type: LayergroupPublishables
        """

        self._publishables = publishables

    @property
    def styles(self):
        """Gets the styles of this Layergroup.  # noqa: E501


        :return: The styles of this Layergroup.  # noqa: E501
        :rtype: LayergroupStyles
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this Layergroup.


        :param styles: The styles of this Layergroup.  # noqa: E501
        :type: LayergroupStyles
        """

        self._styles = styles

    @property
    def metadata_links(self):
        """Gets the metadata_links of this Layergroup.  # noqa: E501


        :return: The metadata_links of this Layergroup.  # noqa: E501
        :rtype: list[LayergroupMetadataLink]
        """
        return self._metadata_links

    @metadata_links.setter
    def metadata_links(self, metadata_links):
        """Sets the metadata_links of this Layergroup.


        :param metadata_links: The metadata_links of this Layergroup.  # noqa: E501
        :type: list[LayergroupMetadataLink]
        """

        self._metadata_links = metadata_links

    @property
    def bounds(self):
        """Gets the bounds of this Layergroup.  # noqa: E501


        :return: The bounds of this Layergroup.  # noqa: E501
        :rtype: LayergroupBounds
        """
        return self._bounds

    @bounds.setter
    def bounds(self, bounds):
        """Sets the bounds of this Layergroup.


        :param bounds: The bounds of this Layergroup.  # noqa: E501
        :type: LayergroupBounds
        """

        self._bounds = bounds

    @property
    def keywords(self):
        """Gets the keywords of this Layergroup.  # noqa: E501


        :return: The keywords of this Layergroup.  # noqa: E501
        :rtype: LayergroupKeywords
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Layergroup.


        :param keywords: The keywords of this Layergroup.  # noqa: E501
        :type: LayergroupKeywords
        """

        self._keywords = keywords

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
        if issubclass(Layergroup, dict):
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
        if not isinstance(other, Layergroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Layergroup):
            return True

        return self.to_dict() != other.to_dict()
