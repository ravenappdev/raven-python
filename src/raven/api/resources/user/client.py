# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ....environment import RavenApiEnvironment
from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ..ids.types.app_id import AppId
from ..ids.types.user_id import UserId
from .types.raven_user import RavenUser


class UserClient:
    def __init__(self, *, environment: RavenApiEnvironment, auth_key: str):
        self._environment = environment
        self.auth_key = auth_key

    def create_or_update(
        self,
        app_id: AppId,
        *,
        user_id: UserId,
        mobile: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        whats_app: typing.Optional[str] = None,
    ) -> RavenUser:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"v1/apps/{app_id}/users"),
            json=jsonable_encoder({"user_id": user_id, "mobile": mobile, "email": email, "whats_app": whats_app}),
            headers=remove_none_from_headers({"Authorization": self.auth_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RavenUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, app_id: AppId, user_id: UserId) -> RavenUser:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}"),
            headers=remove_none_from_headers({"Authorization": self.auth_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RavenUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUserClient:
    def __init__(self, *, environment: RavenApiEnvironment, auth_key: str):
        self._environment = environment
        self.auth_key = auth_key

    async def create_or_update(
        self,
        app_id: AppId,
        *,
        user_id: UserId,
        mobile: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        whats_app: typing.Optional[str] = None,
    ) -> RavenUser:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"v1/apps/{app_id}/users"),
                json=jsonable_encoder({"user_id": user_id, "mobile": mobile, "email": email, "whats_app": whats_app}),
                headers=remove_none_from_headers({"Authorization": self.auth_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RavenUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, app_id: AppId, user_id: UserId) -> RavenUser:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"v1/apps/{app_id}/users/{user_id}"),
                headers=remove_none_from_headers({"Authorization": self.auth_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RavenUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
