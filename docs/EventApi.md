# swagger_client.EventApi

All URIs are relative to *https://api.ravenapp.dev*

| Method                                             | HTTP request                                | Description                                          |
| -------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------- |
| [**send_bulk_event**](EventApi.md#send_bulk_event) | **POST** /v1/apps/{app_id}/events/bulk_send | sends the event in bulk to all the clients specified |
| [**send_event**](EventApi.md#send_event)           | **POST** /v1/apps/{app_id}/events/send      | sends the event to the client specified              |

# **send_bulk_event**

> SuccessResponse send_bulk_event(app_id, event, idempotency_key=idempotency_key)

sends the event in bulk to all the clients specified

This API will send the event in bulk to the clients specified

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import RavenException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EventApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | app id of raven app
event = swagger_client.SendEventBulk() # SendEventBulk | the body for the event that has to be triggered
idempotency_key = 'idempotency_key_example' # str | idempotency key of api (optional)

try:
    # sends the event in bulk to all the clients specified
    api_response = api_instance.send_bulk_event(app_id, event, idempotency_key=idempotency_key)
    pprint(api_response)
except RavenException as e:
    print("Exception when calling EventApi->send_bulk_event: %s\n" % e)
```

### Parameters

| Name                | Type                                  | Description                                     | Notes      |
| ------------------- | ------------------------------------- | ----------------------------------------------- | ---------- |
| **app_id**          | **str**                               | app id of raven app                             |
| **event**           | [**SendEventBulk**](SendEventBulk.md) | the body for the event that has to be triggered |
| **idempotency_key** | **str**                               | idempotency key of api                          | [optional] |

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_event**

> Response send_event(app_id, event, idempotency_key=idempotency_key)

sends the event to the client specified

This API will send the event to the client specified

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import RavenException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.EventApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | app id of raven app
event = swagger_client.SendEvent() # SendEvent | the body for the event that has to be triggered
idempotency_key = 'idempotency_key_example' # str | idempotency key of api (optional)

try:
    # sends the event to the client specified
    api_response = api_instance.send_event(app_id, event, idempotency_key=idempotency_key)
    pprint(api_response)
except RavenException as e:
    print("Exception when calling EventApi->send_event: %s\n" % e)
```

### Parameters

| Name                | Type                          | Description                                     | Notes      |
| ------------------- | ----------------------------- | ----------------------------------------------- | ---------- |
| **app_id**          | **str**                       | app id of raven app                             |
| **event**           | [**SendEvent**](SendEvent.md) | the body for the event that has to be triggered |
| **idempotency_key** | **str**                       | idempotency key of api                          | [optional] |

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
