# Raven

Raven Client SDK for JAVA

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install raven
```

Then import the package:

```python
import raven
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.ravenapp.dev*

| Class         | Method                                         | HTTP request                                | Description                                          |
| ------------- | ---------------------------------------------- | ------------------------------------------- | ---------------------------------------------------- |
| _RavenClient_ | [**send_bulk**](docs/RavenClient.md#send_bulk) | **POST** /v1/apps/{app_id}/events/bulk_send | sends the event in bulk to all the clients specified |
| _RavenClient_ | [**send**](docs/RavenClient.md#send)           | **POST** /v1/apps/{app_id}/events/send      | sends the event to the client specified              |

## Documentation For Models

- [Attachments](docs/Attachments.md)
- [Data](docs/Data.md)
- [EmailOverride](docs/EmailOverride.md)
- [EmailRecipient](docs/EmailRecipient.md)
- [EventOverride](docs/EventOverride.md)
- [Param](docs/Param.md)
- [Properties](docs/Properties.md)
- [ProviderOverride](docs/ProviderOverride.md)
- [PushOverride](docs/PushOverride.md)
- [Response](docs/Response.md)
- [SendEventRequest](docs/SendEventRequest.md)
- [SendEventBulkRequest](docs/SendEventBulkRequest.md)
- [SlackOverride](docs/SlackOverride.md)
- [SlackProfile](docs/SlackProfile.md)
- [SmsOverride](docs/SmsOverride.md)
- [TelegramProfile](docs/TelegramProfile.md)
- [User](docs/User.md)
- [VoiceOverride](docs/VoiceOverride.md)
- [WebhookOverride](docs/WebhookOverride.md)
- [WhatsappOverride](docs/WhatsappOverride.md)

## Author

api@ravenapp.dev
