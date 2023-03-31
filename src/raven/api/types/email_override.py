# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .attachment import Attachment
from .channel_override import ChannelOverride
from .email_message import EmailMessage
from .email_recipient import EmailRecipient


class EmailOverride(ChannelOverride):
    from: EmailRecipient
    cc: typing.List[EmailRecipient]
    bcc: typing.List[EmailRecipient]
    attachments: typing.List[Attachment]
    message: EmailMessage
    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().json(**kwargs_with_defaults)
    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = { "by_alias": True, "exclude_unset": True, **kwargs }
        return super().dict(**kwargs_with_defaults)
    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
