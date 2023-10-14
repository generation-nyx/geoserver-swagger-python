# coding: utf-8

"""
    GeoServer Parameter Extractor

    A parameter extractor rule allows specific request parameters as URL path fragments instead of using the query string. A echo parameter makes sure that certain URL paratemers are added to the capabilities documents backlinks.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ParamsExtractorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_echo_parameter(self, parameter_id, **kwargs):  # noqa: E501
        """Delete an echo parameter  # noqa: E501

        Deletes an echo parameter from the configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_echo_parameter(parameter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parameter_id: The identifier of the  echo parameter to retrieve. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_echo_parameter_with_http_info(parameter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_echo_parameter_with_http_info(parameter_id, **kwargs)  # noqa: E501
            return data

    def delete_echo_parameter_with_http_info(self, parameter_id, **kwargs):  # noqa: E501
        """Delete an echo parameter  # noqa: E501

        Deletes an echo parameter from the configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_echo_parameter_with_http_info(parameter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parameter_id: The identifier of the  echo parameter to retrieve. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parameter_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_echo_parameter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parameter_id' is set
        if self.api_client.client_side_validation and ('parameter_id' not in params or
                                                       params['parameter_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `parameter_id` when calling `delete_echo_parameter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'parameter_id' in params:
            path_params['parameterId'] = params['parameter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/echoes/{parameterId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_rule(self, rule_id, **kwargs):  # noqa: E501
        """Delete a rule  # noqa: E501

        Deletes a rule from the configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_rule(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The identifier of the  rule to retrieve. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_rule_with_http_info(rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_rule_with_http_info(rule_id, **kwargs)  # noqa: E501
            return data

    def delete_rule_with_http_info(self, rule_id, **kwargs):  # noqa: E501
        """Delete a rule  # noqa: E501

        Deletes a rule from the configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_rule_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The identifier of the  rule to retrieve. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in params or
                                                       params['rule_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `rule_id` when calling `delete_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/rules/{ruleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_echo_parameter(self, parameter_id, **kwargs):  # noqa: E501
        """Retrieve a particular echo parameter definition  # noqa: E501

        Controls a particular echo parameter. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/echos/{parameterId}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_echo_parameter(parameter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parameter_id: The identifier of the  echo parameter to retrieve. (required)
        :return: EchoParameter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_echo_parameter_with_http_info(parameter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_echo_parameter_with_http_info(parameter_id, **kwargs)  # noqa: E501
            return data

    def get_echo_parameter_with_http_info(self, parameter_id, **kwargs):  # noqa: E501
        """Retrieve a particular echo parameter definition  # noqa: E501

        Controls a particular echo parameter. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/echos/{parameterId}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_echo_parameter_with_http_info(parameter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parameter_id: The identifier of the  echo parameter to retrieve. (required)
        :return: EchoParameter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parameter_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_echo_parameter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parameter_id' is set
        if self.api_client.client_side_validation and ('parameter_id' not in params or
                                                       params['parameter_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `parameter_id` when calling `get_echo_parameter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'parameter_id' in params:
            path_params['parameterId'] = params['parameter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/echoes/{parameterId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EchoParameter',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_echo_parameters(self, **kwargs):  # noqa: E501
        """Get a list of echo parameters  # noqa: E501

        List all echo parameters currently configured.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_echo_parameters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EchoParameters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_echo_parameters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_echo_parameters_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_echo_parameters_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of echo parameters  # noqa: E501

        List all echo parameters currently configured.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_echo_parameters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EchoParameters
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_echo_parameters" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/echoes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EchoParameters',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rule(self, rule_id, **kwargs):  # noqa: E501
        """Retrieve a particular rule definition  # noqa: E501

        Controls a particular rule . Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/echos/{parameterId}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rule(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The identifier of the  rule to retrieve. (required)
        :return: Rule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rule_with_http_info(rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rule_with_http_info(rule_id, **kwargs)  # noqa: E501
            return data

    def get_rule_with_http_info(self, rule_id, **kwargs):  # noqa: E501
        """Retrieve a particular rule definition  # noqa: E501

        Controls a particular rule . Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/echos/{parameterId}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rule_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The identifier of the  rule to retrieve. (required)
        :return: Rule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in params or
                                                       params['rule_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `rule_id` when calling `get_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/rules/{ruleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rules(self, **kwargs):  # noqa: E501
        """Get a list of rules  # noqa: E501

        List all rules currently configured.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Rules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_rules_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of rules  # noqa: E501

        List all rules currently configured.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Rules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_echo_parameter(self, **kwargs):  # noqa: E501
        """Create a new echo parameter  # noqa: E501

        Adds a new echo parameter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_echo_parameter(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EchoParameter body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_echo_parameter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_echo_parameter_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_echo_parameter_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new echo parameter  # noqa: E501

        Adds a new echo parameter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_echo_parameter_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EchoParameter body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_echo_parameter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/echoes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_rule(self, **kwargs):  # noqa: E501
        """Create a new rule  # noqa: E501

        Adds a new rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_rule(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Rule body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_rule_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_rule_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_rule_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new rule  # noqa: E501

        Adds a new rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_rule_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Rule body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_rule" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_echo_parameter(self, parameter_id, **kwargs):  # noqa: E501
        """Modify an echo parametr  # noqa: E501

        Modify an echo parameter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_echo_parameter(parameter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parameter_id: The identifier of the  echo parameter to retrieve. (required)
        :param EchoParameter body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_echo_parameter_with_http_info(parameter_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_echo_parameter_with_http_info(parameter_id, **kwargs)  # noqa: E501
            return data

    def put_echo_parameter_with_http_info(self, parameter_id, **kwargs):  # noqa: E501
        """Modify an echo parametr  # noqa: E501

        Modify an echo parameter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_echo_parameter_with_http_info(parameter_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parameter_id: The identifier of the  echo parameter to retrieve. (required)
        :param EchoParameter body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parameter_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_echo_parameter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parameter_id' is set
        if self.api_client.client_side_validation and ('parameter_id' not in params or
                                                       params['parameter_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `parameter_id` when calling `put_echo_parameter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'parameter_id' in params:
            path_params['parameterId'] = params['parameter_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/echoes/{parameterId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_rule(self, rule_id, **kwargs):  # noqa: E501
        """Modify a rule  # noqa: E501

        Modify a rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_rule(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The identifier of the  echo parameter to retrieve. (required)
        :param Rule body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_rule_with_http_info(rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_rule_with_http_info(rule_id, **kwargs)  # noqa: E501
            return data

    def put_rule_with_http_info(self, rule_id, **kwargs):  # noqa: E501
        """Modify a rule  # noqa: E501

        Modify a rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_rule_with_http_info(rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rule_id: The identifier of the  echo parameter to retrieve. (required)
        :param Rule body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in params or
                                                       params['rule_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `rule_id` when calling `put_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/params-extractor/rules/{ruleId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
