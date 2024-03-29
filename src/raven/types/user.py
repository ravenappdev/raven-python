# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from ..resources.ids.types.user_id import UserId
from ..resources.user.types.slack_profile import SlackProfile
from ..resources.user.types.telegram_profile import TelegramProfile


class User(pydantic.BaseModel):
    user_id: typing.Optional[UserId] = pydantic.Field(
        description=(
            "userId to send the notifications to. \n"
            "This is  your own user identifier which you have used to [create user on Raven](https://docs.raven.dev/api-reference/create-user)\n"
        )
    )
    email: typing.Optional[str]
    mobile: typing.Optional[str] = pydantic.Field(description=("mobile with country code prefix (e.g +91)\n"))
    whatsapp_mobile: typing.Optional[str] = pydantic.Field(
        description=("mobile with country code prefix (e.g. +91).\n" "if empty, `mobile` is considered for whatsapp\n")
    )
    onesignal_external_id: typing.Optional[str] = pydantic.Field(
        description=("[OneSignal external user IDs](https://documentation.onesignal.com/docs/external-user-ids)\n")
    )
    onesignal_player_ids: typing.Optional[typing.List[str]]
    fcm_tokens: typing.Optional[typing.List[str]] = pydantic.Field(
        description=('List of fcm tokens.  eg. ["<fcmtoken1", "<fcmtoken2>"]\n')
    )
    ios_tokens: typing.Optional[typing.List[str]]
    slack: typing.Optional[SlackProfile]
    telegram: typing.Optional[TelegramProfile]
    fcm_topic: typing.Optional[str]
    fcm_device_group: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
