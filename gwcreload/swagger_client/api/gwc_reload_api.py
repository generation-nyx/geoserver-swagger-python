# coding: utf-8

"""
    GeoWebCache Reloading

    Reloading a GeoWebCache instance after changing configurations.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class GwcReloadApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reload_post(self, **kwargs):  # noqa: E501
        """Reloads GWC settings/  # noqa: E501

        Reloads the GeoWebCache settings after making changes to the configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reload_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str configuration_name: The string value of the configuration ie. \"reload_configuration=1\"
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reload_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.reload_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def reload_post_with_http_info(self, **kwargs):  # noqa: E501
        """Reloads GWC settings/  # noqa: E501

        Reloads the GeoWebCache settings after making changes to the configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reload_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str configuration_name: The string value of the configuration ie. \"reload_configuration=1\"
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['configuration_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reload_post" % key
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
        if 'configuration_name' in params:
            body_params = params['configuration_name']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/reload', 'POST',
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