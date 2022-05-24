# coding: utf-8

"""
    Raven API

    This is OpenAPI defintion for the APIs of Raven.  You can find out more about Raven at [https://ravenapp.dev/](https://ravenapp.dev/).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@ravenapp.dev
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class SendEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'event': 'str',
        'user': 'User',
        'data': 'Data',
        'schedule_at': 'str',
        'override': 'EventOverride'
    }

    attribute_map = {
        'event': 'event',
        'user': 'user',
        'data': 'data',
        'schedule_at': 'schedule_at',
        'override': 'override'
    }

    def __init__(self, event=None, user=None, data=None, schedule_at=None, override=None, _configuration=None):  # noqa: E501
        """SendEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event = None
        self._user = None
        self._data = None
        self._schedule_at = None
        self._override = None
        self.discriminator = None

        self.event = event
        self.user = user
        if data is not None:
            self.data = data
        if schedule_at is not None:
            self.schedule_at = schedule_at
        if override is not None:
            self.override = override

    @property
    def event(self):
        """Gets the event of this SendEvent.  # noqa: E501


        :return: The event of this SendEvent.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this SendEvent.


        :param event: The event of this SendEvent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def user(self):
        """Gets the user of this SendEvent.  # noqa: E501


        :return: The user of this SendEvent.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SendEvent.


        :param user: The user of this SendEvent.  # noqa: E501
        :type: User
        """
        if self._configuration.client_side_validation and user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def data(self):
        """Gets the data of this SendEvent.  # noqa: E501


        :return: The data of this SendEvent.  # noqa: E501
        :rtype: Data
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SendEvent.


        :param data: The data of this SendEvent.  # noqa: E501
        :type: Data
        """

        self._data = data

    @property
    def schedule_at(self):
        """Gets the schedule_at of this SendEvent.  # noqa: E501


        :return: The schedule_at of this SendEvent.  # noqa: E501
        :rtype: str
        """
        return self._schedule_at

    @schedule_at.setter
    def schedule_at(self, schedule_at):
        """Sets the schedule_at of this SendEvent.


        :param schedule_at: The schedule_at of this SendEvent.  # noqa: E501
        :type: str
        """

        self._schedule_at = schedule_at

    @property
    def override(self):
        """Gets the override of this SendEvent.  # noqa: E501


        :return: The override of this SendEvent.  # noqa: E501
        :rtype: EventOverride
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this SendEvent.


        :param override: The override of this SendEvent.  # noqa: E501
        :type: EventOverride
        """

        self._override = override

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SendEvent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendEvent):
            return True

        return self.to_dict() != other.to_dict()
