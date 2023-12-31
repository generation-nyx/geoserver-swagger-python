# coding: utf-8

"""
    OWS Services

    An OWS service refers to any of the OGC services that GeoServer supports, such as WFS, WMS, and WCS. These endpoints controls the settings of these services.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WMTSInfo(object):
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
        'enabled': 'bool',
        'name': 'str',
        'title': 'str',
        'maintainer': 'str',
        'abstrct': 'str',
        'access_constraints': 'str',
        'fees': 'str',
        'versions': 'WMSInfoVersions',
        'keywords': 'list[str]',
        'metadata_link': 'list[WMSInfoMetadataLink]',
        'cite_compliant': 'bool',
        'online_resource': 'str',
        'schema_base_url': 'str',
        'verbose': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'name': 'name',
        'title': 'title',
        'maintainer': 'maintainer',
        'abstrct': 'abstrct',
        'access_constraints': 'accessConstraints',
        'fees': 'fees',
        'versions': 'versions',
        'keywords': 'keywords',
        'metadata_link': 'metadataLink',
        'cite_compliant': 'citeCompliant',
        'online_resource': 'onlineResource',
        'schema_base_url': 'schemaBaseURL',
        'verbose': 'verbose'
    }

    def __init__(self, enabled=None, name=None, title=None, maintainer=None, abstrct=None, access_constraints=None, fees=None, versions=None, keywords=None, metadata_link=None, cite_compliant=None, online_resource=None, schema_base_url=None, verbose=None, _configuration=None):  # noqa: E501
        """WMTSInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._name = None
        self._title = None
        self._maintainer = None
        self._abstrct = None
        self._access_constraints = None
        self._fees = None
        self._versions = None
        self._keywords = None
        self._metadata_link = None
        self._cite_compliant = None
        self._online_resource = None
        self._schema_base_url = None
        self._verbose = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if maintainer is not None:
            self.maintainer = maintainer
        if abstrct is not None:
            self.abstrct = abstrct
        if access_constraints is not None:
            self.access_constraints = access_constraints
        if fees is not None:
            self.fees = fees
        if versions is not None:
            self.versions = versions
        if keywords is not None:
            self.keywords = keywords
        if metadata_link is not None:
            self.metadata_link = metadata_link
        if cite_compliant is not None:
            self.cite_compliant = cite_compliant
        if online_resource is not None:
            self.online_resource = online_resource
        if schema_base_url is not None:
            self.schema_base_url = schema_base_url
        if verbose is not None:
            self.verbose = verbose

    @property
    def enabled(self):
        """Gets the enabled of this WMTSInfo.  # noqa: E501

        Status of the service  # noqa: E501

        :return: The enabled of this WMTSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WMTSInfo.

        Status of the service  # noqa: E501

        :param enabled: The enabled of this WMTSInfo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """Gets the name of this WMTSInfo.  # noqa: E501

        Name of the service. This value is unique among all instances of ServiceInfo and can be used as an identifier.  # noqa: E501

        :return: The name of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WMTSInfo.

        Name of the service. This value is unique among all instances of ServiceInfo and can be used as an identifier.  # noqa: E501

        :param name: The name of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this WMTSInfo.  # noqa: E501

        Title of the service  # noqa: E501

        :return: The title of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WMTSInfo.

        Title of the service  # noqa: E501

        :param title: The title of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def maintainer(self):
        """Gets the maintainer of this WMTSInfo.  # noqa: E501

        Maintainer of the service  # noqa: E501

        :return: The maintainer of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        """Sets the maintainer of this WMTSInfo.

        Maintainer of the service  # noqa: E501

        :param maintainer: The maintainer of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._maintainer = maintainer

    @property
    def abstrct(self):
        """Gets the abstrct of this WMTSInfo.  # noqa: E501

        Description of the service  # noqa: E501

        :return: The abstrct of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._abstrct

    @abstrct.setter
    def abstrct(self, abstrct):
        """Sets the abstrct of this WMTSInfo.

        Description of the service  # noqa: E501

        :param abstrct: The abstrct of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._abstrct = abstrct

    @property
    def access_constraints(self):
        """Gets the access_constraints of this WMTSInfo.  # noqa: E501

        Access constraints  # noqa: E501

        :return: The access_constraints of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._access_constraints

    @access_constraints.setter
    def access_constraints(self, access_constraints):
        """Sets the access_constraints of this WMTSInfo.

        Access constraints  # noqa: E501

        :param access_constraints: The access_constraints of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._access_constraints = access_constraints

    @property
    def fees(self):
        """Gets the fees of this WMTSInfo.  # noqa: E501

        Any fees associated with the service  # noqa: E501

        :return: The fees of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this WMTSInfo.

        Any fees associated with the service  # noqa: E501

        :param fees: The fees of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._fees = fees

    @property
    def versions(self):
        """Gets the versions of this WMTSInfo.  # noqa: E501


        :return: The versions of this WMTSInfo.  # noqa: E501
        :rtype: WMSInfoVersions
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this WMTSInfo.


        :param versions: The versions of this WMTSInfo.  # noqa: E501
        :type: WMSInfoVersions
        """

        self._versions = versions

    @property
    def keywords(self):
        """Gets the keywords of this WMTSInfo.  # noqa: E501

        Keywords associated with the service.  # noqa: E501

        :return: The keywords of this WMTSInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this WMTSInfo.

        Keywords associated with the service.  # noqa: E501

        :param keywords: The keywords of this WMTSInfo.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def metadata_link(self):
        """Gets the metadata_link of this WMTSInfo.  # noqa: E501


        :return: The metadata_link of this WMTSInfo.  # noqa: E501
        :rtype: list[WMSInfoMetadataLink]
        """
        return self._metadata_link

    @metadata_link.setter
    def metadata_link(self, metadata_link):
        """Sets the metadata_link of this WMTSInfo.


        :param metadata_link: The metadata_link of this WMTSInfo.  # noqa: E501
        :type: list[WMSInfoMetadataLink]
        """

        self._metadata_link = metadata_link

    @property
    def cite_compliant(self):
        """Gets the cite_compliant of this WMTSInfo.  # noqa: E501

        Status of service CITE compliance  # noqa: E501

        :return: The cite_compliant of this WMTSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._cite_compliant

    @cite_compliant.setter
    def cite_compliant(self, cite_compliant):
        """Sets the cite_compliant of this WMTSInfo.

        Status of service CITE compliance  # noqa: E501

        :param cite_compliant: The cite_compliant of this WMTSInfo.  # noqa: E501
        :type: bool
        """

        self._cite_compliant = cite_compliant

    @property
    def online_resource(self):
        """Gets the online_resource of this WMTSInfo.  # noqa: E501

        URL resource  # noqa: E501

        :return: The online_resource of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._online_resource

    @online_resource.setter
    def online_resource(self, online_resource):
        """Sets the online_resource of this WMTSInfo.

        URL resource  # noqa: E501

        :param online_resource: The online_resource of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._online_resource = online_resource

    @property
    def schema_base_url(self):
        """Gets the schema_base_url of this WMTSInfo.  # noqa: E501

        Base URL for the schemas describing the service  # noqa: E501

        :return: The schema_base_url of this WMTSInfo.  # noqa: E501
        :rtype: str
        """
        return self._schema_base_url

    @schema_base_url.setter
    def schema_base_url(self, schema_base_url):
        """Sets the schema_base_url of this WMTSInfo.

        Base URL for the schemas describing the service  # noqa: E501

        :param schema_base_url: The schema_base_url of this WMTSInfo.  # noqa: E501
        :type: str
        """

        self._schema_base_url = schema_base_url

    @property
    def verbose(self):
        """Gets the verbose of this WMTSInfo.  # noqa: E501

        Flag indicating if the service should be verbose  # noqa: E501

        :return: The verbose of this WMTSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._verbose

    @verbose.setter
    def verbose(self, verbose):
        """Sets the verbose of this WMTSInfo.

        Flag indicating if the service should be verbose  # noqa: E501

        :param verbose: The verbose of this WMTSInfo.  # noqa: E501
        :type: bool
        """

        self._verbose = verbose

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
        if issubclass(WMTSInfo, dict):
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
        if not isinstance(other, WMTSInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WMTSInfo):
            return True

        return self.to_dict() != other.to_dict()
