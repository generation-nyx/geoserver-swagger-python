# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WorkspacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_workspace(self, workspace_name, **kwargs):  # noqa: E501
        """delete_workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspace(workspace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_name: name of workspace (required)
        :param bool recurse: delete workspace contents (default false)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_workspace_with_http_info(workspace_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_workspace_with_http_info(workspace_name, **kwargs)  # noqa: E501
            return data

    def delete_workspace_with_http_info(self, workspace_name, **kwargs):  # noqa: E501
        """delete_workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspace_with_http_info(workspace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_name: name of workspace (required)
        :param bool recurse: delete workspace contents (default false)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_name', 'recurse']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_name' is set
        if self.api_client.client_side_validation and ('workspace_name' not in params or
                                                       params['workspace_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_name` when calling `delete_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_name' in params:
            path_params['workspaceName'] = params['workspace_name']  # noqa: E501

        query_params = []
        if 'recurse' in params:
            query_params.append(('recurse', params['recurse']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspaceName}', 'DELETE',
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

    def delete_workspaces(self, **kwargs):  # noqa: E501
        """delete_workspaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_workspaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_workspaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_workspaces_with_http_info(self, **kwargs):  # noqa: E501
        """delete_workspaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspaces_with_http_info(async_req=True)
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
                    " to method delete_workspaces" % key
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
            '/workspaces', 'DELETE',
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

    def get_workspace(self, workspace_name, **kwargs):  # noqa: E501
        """Retrieve a layer group  # noqa: E501

        Retrieves a single workspace definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace(workspace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_name: the name of the workspace to fetch (required)
        :param bool quiet_on_not_found: The quietOnNotFound parameter avoids logging an exception when the workspace is not present. Note that 404 status code will still be returned.
        :return: WorkspaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workspace_with_http_info(workspace_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_with_http_info(workspace_name, **kwargs)  # noqa: E501
            return data

    def get_workspace_with_http_info(self, workspace_name, **kwargs):  # noqa: E501
        """Retrieve a layer group  # noqa: E501

        Retrieves a single workspace definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}.xml\" for XML).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_with_http_info(workspace_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_name: the name of the workspace to fetch (required)
        :param bool quiet_on_not_found: The quietOnNotFound parameter avoids logging an exception when the workspace is not present. Note that 404 status code will still be returned.
        :return: WorkspaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_name', 'quiet_on_not_found']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_name' is set
        if self.api_client.client_side_validation and ('workspace_name' not in params or
                                                       params['workspace_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_name` when calling `get_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_name' in params:
            path_params['workspaceName'] = params['workspace_name']  # noqa: E501

        query_params = []
        if 'quiet_on_not_found' in params:
            query_params.append(('quietOnNotFound', params['quiet_on_not_found']))  # noqa: E501

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
            '/workspaces/{workspaceName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkspaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspaces(self, **kwargs):  # noqa: E501
        """Get a list of workspaces  # noqa: E501

        Displays a list of all workspaces on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WorkspacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workspaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_workspaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_workspaces_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of workspaces  # noqa: E501

        Displays a list of all workspaces on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces.xml\" for XML)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WorkspacesResponse
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
                    " to method get_workspaces" % key
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
            '/workspaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkspacesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_workspace(self, **kwargs):  # noqa: E501
        """post_workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_workspace_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_workspace_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_workspace_with_http_info(self, **kwargs):  # noqa: E501
        """post_workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspace_with_http_info(async_req=True)
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
                    " to method post_workspace" % key
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
            '/workspaces/{workspaceName}', 'POST',
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

    def post_workspaces(self, workspace_body, **kwargs):  # noqa: E501
        """add a new workspace to GeoServer  # noqa: E501

        Adds a new workspace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspaces(workspace_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Workspace workspace_body: The layer group body information to upload. (required)
        :param bool default: New workspace will be the used as the default. Allowed values are true or false,  The default value is false.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_workspaces_with_http_info(workspace_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_workspaces_with_http_info(workspace_body, **kwargs)  # noqa: E501
            return data

    def post_workspaces_with_http_info(self, workspace_body, **kwargs):  # noqa: E501
        """add a new workspace to GeoServer  # noqa: E501

        Adds a new workspace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_workspaces_with_http_info(workspace_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Workspace workspace_body: The layer group body information to upload. (required)
        :param bool default: New workspace will be the used as the default. Allowed values are true or false,  The default value is false.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_body', 'default']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workspaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_body' is set
        if self.api_client.client_side_validation and ('workspace_body' not in params or
                                                       params['workspace_body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_body` when calling `post_workspaces`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'default' in params:
            query_params.append(('default', params['default']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workspace_body' in params:
            body_params = params['workspace_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html', 'application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workspaces', 'POST',
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

    def put_workspace(self, workspace_name, workspace_body, **kwargs):  # noqa: E501
        """Update a workspace  # noqa: E501

        takes the body of the post and modifies the workspace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_workspace(workspace_name, workspace_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_name: name of workspace (required)
        :param Workspace workspace_body: The layer group body information to upload. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_workspace_with_http_info(workspace_name, workspace_body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_workspace_with_http_info(workspace_name, workspace_body, **kwargs)  # noqa: E501
            return data

    def put_workspace_with_http_info(self, workspace_name, workspace_body, **kwargs):  # noqa: E501
        """Update a workspace  # noqa: E501

        takes the body of the post and modifies the workspace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_workspace_with_http_info(workspace_name, workspace_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace_name: name of workspace (required)
        :param Workspace workspace_body: The layer group body information to upload. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_name', 'workspace_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_name' is set
        if self.api_client.client_side_validation and ('workspace_name' not in params or
                                                       params['workspace_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_name` when calling `put_workspace`")  # noqa: E501
        # verify the required parameter 'workspace_body' is set
        if self.api_client.client_side_validation and ('workspace_body' not in params or
                                                       params['workspace_body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `workspace_body` when calling `put_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace_name' in params:
            path_params['workspaceName'] = params['workspace_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workspace_body' in params:
            body_params = params['workspace_body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspaceName}', 'PUT',
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

    def put_workspaces(self, **kwargs):  # noqa: E501
        """put_workspaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_workspaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_workspaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_workspaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_workspaces_with_http_info(self, **kwargs):  # noqa: E501
        """put_workspaces  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_workspaces_with_http_info(async_req=True)
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
                    " to method put_workspaces" % key
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
            '/workspaces', 'PUT',
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
