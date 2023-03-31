# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .channel_preference import ChannelPreference


class ChannelPreferences(pydantic.BaseModel):
    sms: typing.Optional[ChannelPreference]
    push: typing.Optional[ChannelPreference]
    whatsapp: typing.Optional[ChannelPreference]
    email: typing.Optional[ChannelPreference]
    slack: typing.Optional[ChannelPreference]
    voice: typing.Optional[ChannelPreference]
    teams: typing.Optional[ChannelPreference]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}