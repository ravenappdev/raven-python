# RavenClient

All URIs are relative to *https://api.ravenapp.dev*

| Method                                    | HTTP request                                | Description                                          |
| ----------------------------------------- | ------------------------------------------- | ---------------------------------------------------- |
| [**send_bulk**](RavenClient.md#send_bulk) | **POST** /v1/apps/{app_id}/events/bulk_send | sends the event in bulk to all the clients specified |
| [**send**](RavenClient.md#send)           | **POST** /v1/apps/{app_id}/events/send      | sends the event to the client specified              |

# **send_bulk**

> Response send_bulk(app_id, event, idempotency_key=idempotency_key)

sends the event in bulk to all the clients specified

This API will send the event in bulk to the clients specified

### Example

```python
from __future__ import print_function
import time
import raven
from raven import RavenException
from pprint import pprint


# create an instance of the API class
api_instance = raven.RavenClient("YOUR API KEY")
app_id = 'app_id_example' # str | app id of raven app
event = raven.SendEventBulk() # SendEventBulk | the body for the event that has to be triggered
idempotency_key = 'idempotency_key_example' # str | idempotency key of api (optional)

try:
    # sends the event in bulk to all the clients specified
    api_response = api_instance.send_bulk(app_id, event, idempotency_key=idempotency_key)
    pprint(api_response)
except RavenException as e:
    print("Exception when calling RavenClient->send_bulk: %s\n" % e)

```

### Parameters

| Name                | Type                                         | Description                                     | Notes      |
| ------------------- | -------------------------------------------- | ----------------------------------------------- | ---------- |
| **app_id**          | **str**                                      | app id of raven app                             |
| **event**           | [**SendEventBulk**](SendEventBulkRequest.md) | the body for the event that has to be triggered |
| **idempotency_key** | **str**                                      | idempotency key of api                          | [optional] |

### Return type

[**Response**](Response.md)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**

> Response send(app_id, event, idempotency_key=idempotency_key)

sends the event to the client specified

This API will send the event to the client specified

### Example

```python
from __future__ import print_function
import time
import raven
from raven import RavenException
from pprint import pprint


# create an instance of the API class
api_instance = raven.RavenClient("YOUR API KEY")
app_id = 'app_id_example' # str | app id of raven app
event = raven.SendEvent() # SendEvent | the body for the event that has to be triggered
idempotency_key = 'idempotency_key_example' # str | idempotency key of api (optional)

try:
    # sends the event in to all the clients specified
    api_response = api_instance.send(app_id, event, idempotency_key=idempotency_key)
    pprint(api_response)
except RavenException as e:
    print("Exception when calling RavenClient->send: %s\n" % e)

```

### Parameters

| Name                | Type                                 | Description                                     | Notes      |
| ------------------- | ------------------------------------ | ----------------------------------------------- | ---------- |
| **app_id**          | **str**                              | app id of raven app                             |
| **event**           | [**SendEvent**](SendEventRequest.md) | the body for the event that has to be triggered |
| **idempotency_key** | **str**                              | idempotency key of api                          | [optional] |

### Return type

[**Response**](Response.md)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
