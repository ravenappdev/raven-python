# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ....environment import RavenApiEnvironment
from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ..ids.types.app_id import AppId
from ..ids.types.device_id import DeviceId
from ..ids.types.user_id import UserId
from .types.device import Device


class DeviceClient:
    def __init__(self, *, environment: RavenApiEnvironment, auth_key: str):
        self._environment = environment
        self.auth_key = auth_key

    def add(self, app_id: AppId, user_id: UserId, *, request: Device) -> Device:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers({"Authorization": self.auth_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Device, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, app_id: AppId, user_id: UserId, device_id: DeviceId, *, request: Device) -> Device:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices/{device_id}"
            ),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers({"Authorization": self.auth_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Device, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, app_id: AppId, user_id: UserId, device_id: DeviceId) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices/{device_id}"
            ),
            headers=remove_none_from_headers({"Authorization": self.auth_key}),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_device(self, app_id: AppId, user_id: UserId, device_id: DeviceId) -> Device:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices/{device_id}"
            ),
            headers=remove_none_from_headers({"Authorization": self.auth_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Device, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDeviceClient:
    def __init__(self, *, environment: RavenApiEnvironment, auth_key: str):
        self._environment = environment
        self.auth_key = auth_key

    async def add(self, app_id: AppId, user_id: UserId, *, request: Device) -> Device:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers({"Authorization": self.auth_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Device, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, app_id: AppId, user_id: UserId, device_id: DeviceId, *, request: Device) -> Device:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices/{device_id}"
                ),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers({"Authorization": self.auth_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Device, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, app_id: AppId, user_id: UserId, device_id: DeviceId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices/{device_id}"
                ),
                headers=remove_none_from_headers({"Authorization": self.auth_key}),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_device(self, app_id: AppId, user_id: UserId, device_id: DeviceId) -> Device:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}/devices/{device_id}"
                ),
                headers=remove_none_from_headers({"Authorization": self.auth_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Device, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
