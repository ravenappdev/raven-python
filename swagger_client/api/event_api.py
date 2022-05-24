from __future__ import absolute_import

import re  

import six

from swagger_client.api_client import ApiClient


class EventApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def send_bulk(self, app_id, event, **kwargs):  
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_bulk_with_http_info(app_id, event, **kwargs)  
        else:
            (data) = self.send_bulk_with_http_info(app_id, event, **kwargs)  
            return data

    def send_bulk_with_http_info(self, app_id, event, **kwargs):  
        """sends the event in bulk to all the clients specified  

        This API will send the event in bulk to the clients specified  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_bulk_with_http_info(app_id, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: app id of raven app (required)
        :param SendEventBulk event: the body for the event that has to be triggered (required)
        :param str idempotency_key: idempotency key of api
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'event', 'idempotency_key']  
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_bulk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in params or
                                                       params['app_id'] is None):  
            raise ValueError("Missing the required parameter `app_id` when calling `send_bulk`")  
        # verify the required parameter 'event' is set
        if self.api_client.client_side_validation and ('event' not in params or
                                                       params['event'] is None):  
            raise ValueError("Missing the required parameter `event` when calling `send_bulk`")  

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['app_id'] = params['app_id']  

        query_params = []

        header_params = {}
        if 'idempotency_key' in params:
            header_params['Idempotency-Key'] = params['idempotency_key']  

        form_params = []
        local_var_files = {}

        body_params = None
        if 'event' in params:
            body_params = params['event']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  
            ['application/json'])  

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  

        return self.api_client.call_api(
            '/v1/apps/{app_id}/events/bulk_send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send(self, app_id, event, **kwargs):  
        
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_with_http_info(app_id, event, **kwargs)  
        else:
            (data) = self.send_with_http_info(app_id, event, **kwargs)  
            return data

    def send_with_http_info(self, app_id, event, **kwargs):  
        """sends the event to the client specified  

        This API will send the event to the client specified  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_with_http_info(app_id, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: app id of raven app (required)
        :param SendEvent event: the body for the event that has to be triggered (required)
        :param str idempotency_key: idempotency key of api
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'event', 'idempotency_key']  
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and ('app_id' not in params or
                                                       params['app_id'] is None):  
            raise ValueError("Missing the required parameter `app_id` when calling `send`")  
        # verify the required parameter 'event' is set
        if self.api_client.client_side_validation and ('event' not in params or
                                                       params['event'] is None):  
            raise ValueError("Missing the required parameter `event` when calling `send`")  

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['app_id'] = params['app_id']  

        query_params = []

        header_params = {}
        if 'idempotency_key' in params:
            header_params['Idempotency-Key'] = params['idempotency_key']  

        form_params = []
        local_var_files = {}

        body_params = None
        if 'event' in params:
            body_params = params['event']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  
            ['application/json'])  

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  

        return self.api_client.call_api(
            '/v1/apps/{app_id}/events/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
