# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .event_override import EventOverride
from .user import User


class BatchEvent(pydantic.BaseModel):
    data: typing.Dict[str, typing.Any] = pydantic.Field(
        description=("{\n" '"param1" : "<value1>",\n' '"param2" : "<value2>",\n' '"param3" : object/array"\n' "}\n")
    )
    user: typing.Optional[User]
    override: typing.Optional[EventOverride]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
