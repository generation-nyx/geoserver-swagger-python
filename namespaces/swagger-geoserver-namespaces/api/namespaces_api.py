# coding: utf-8

"""
    GeoServer Namespace

    A namespace is a uniquely identifiable grouping of feature types. It is identified by a prefix and a URI.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger-geoserver-namespaces.api_client import ApiClient


class NamespacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_namespace(self, namespace_name, **kwargs):  # noqa: E501
        """Delete a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace(namespace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_name: Name of the namespace (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_namespace_with_http_info(namespace_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_namespace_with_http_info(namespace_name, **kwargs)  # noqa: E501
            return data

    def delete_namespace_with_http_info(self, namespace_name, **kwargs):  # noqa: E501
        """Delete a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace_with_http_info(namespace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_name: Name of the namespace (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace_name' is set
        if self.api_client.client_side_validation and ('namespace_name' not in params or
                                                       params['namespace_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace_name` when calling `delete_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespaceName}', 'DELETE',
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

    def delete_namespaces(self, **kwargs):  # noqa: E501
        """delete_namespaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_namespaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_namespaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_namespaces_with_http_info(self, **kwargs):  # noqa: E501
        """delete_namespaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method delete_namespaces" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces', 'DELETE',
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

    def get_namespace(self, namespace_name, **kwargs):  # noqa: E501
        """Retrieve a namespace  # noqa: E501

        Retrieves a single namespace definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/namespaces/{namespace}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace(namespace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_name: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :return: NamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_namespace_with_http_info(namespace_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_namespace_with_http_info(namespace_name, **kwargs)  # noqa: E501
            return data

    def get_namespace_with_http_info(self, namespace_name, **kwargs):  # noqa: E501
        """Retrieve a namespace  # noqa: E501

        Retrieves a single namespace definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/namespaces/{namespace}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace_with_http_info(namespace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_name: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :return: NamespaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace_name' is set
        if self.api_client.client_side_validation and ('namespace_name' not in params or
                                                       params['namespace_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace_name` when calling `get_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespaceName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamespaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_namespaces(self, **kwargs):  # noqa: E501
        """Get a list of namespaces  # noqa: E501

        Displays a list of all namespaces on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/namespaces.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NamespacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_namespaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_namespaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_namespaces_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of namespaces  # noqa: E501

        Displays a list of all namespaces on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/namespaces.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NamespacesResponse
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
                    " to method get_namespaces" % key
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
            ['text/html', 'application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamespacesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_namespace(self, **kwargs):  # noqa: E501
        """post_namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_namespace(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_namespace_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_namespace_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_namespace_with_http_info(self, **kwargs):  # noqa: E501
        """post_namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_namespace_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method post_namespace" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespaceName}', 'POST',
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

    def post_namespaces(self, namespace_body, **kwargs):  # noqa: E501
        """Add a new namespace to GeoServer  # noqa: E501

        Adds a new namespace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_namespaces(namespace_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Namespace namespace_body: The layer group body information to upload. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_namespaces_with_http_info(namespace_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_namespaces_with_http_info(namespace_body, **kwargs)  # noqa: E501
            return data

    def post_namespaces_with_http_info(self, namespace_body, **kwargs):  # noqa: E501
        """Add a new namespace to GeoServer  # noqa: E501

        Adds a new namespace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_namespaces_with_http_info(namespace_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Namespace namespace_body: The layer group body information to upload. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_namespaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace_body' is set
        if self.api_client.client_side_validation and ('namespace_body' not in params or
                                                       params['namespace_body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace_body` when calling `post_namespaces`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'namespace_body' in params:
            body_params = params['namespace_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html', 'application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces', 'POST',
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

    def put_namespace(self, namespace_name, **kwargs):  # noqa: E501
        """Update a namespace  # noqa: E501

        Takes the body of the put and modifies the namespace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_namespace(namespace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_name: Name of namespace, or \"default\" to set the default namespace using the namespace prefix in the body of the post. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_namespace_with_http_info(namespace_name, **kwargs)  # noqa: E501
        else:
            (data) = self.put_namespace_with_http_info(namespace_name, **kwargs)  # noqa: E501
            return data

    def put_namespace_with_http_info(self, namespace_name, **kwargs):  # noqa: E501
        """Update a namespace  # noqa: E501

        Takes the body of the put and modifies the namespace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_namespace_with_http_info(namespace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_name: Name of namespace, or \"default\" to set the default namespace using the namespace prefix in the body of the post. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace_name' is set
        if self.api_client.client_side_validation and ('namespace_name' not in params or
                                                       params['namespace_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `namespace_name` when calling `put_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace_name' in params:
            path_params['namespaceName'] = params['namespace_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespaceName}', 'PUT',
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

    def put_namespaces(self, **kwargs):  # noqa: E501
        """put_namespaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_namespaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_namespaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_namespaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_namespaces_with_http_info(self, **kwargs):  # noqa: E501
        """put_namespaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_namespaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method put_namespaces" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/namespaces', 'PUT',
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