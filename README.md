# Raven Python Library

[![pypi](https://img.shields.io/pypi/v/ravendev.svg)](https://pypi.python.org/pypi/ravendev)


## Documentation

API documentation is available at <https://docs.ravenapp.dev/introduction>.

## Installation

Add this dependency to your project's build file:

```bash
pip install ravendev
# or
poetry add ravendev
```

## Usage

```python
from ravendev.client import RavenApi

raven = RavenApi(auth_key="YOUR_AUTH_KEY")

raven.send(
  app_id="some-app-id",
  event="event",
  data={},
)
```

## Async client

This SDK also includes an async client, which supports the `await` syntax:

```python
from ravendev.client import AsyncRavenApi

raven = AsyncRavenApi(auth_key="YOUR_AUTH_KEY")

async def send_event() -> None:
  await raven.send(
    app_id="some-app-id",
    event="event",
    data={},
  )
```

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your build.gradle file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest [opening an issue](https://github.com/ravenappdev/raven-java) first to discuss with us!

On the other hand, contributions to the README are always very welcome!
