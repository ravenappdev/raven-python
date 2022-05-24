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


class SlackProfile(object):
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
        'access_token': 'str',
        'email': 'str',
        'channel_id': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'email': 'email',
        'channel_id': 'channel_id'
    }

    def __init__(self, access_token=None, email=None, channel_id=None, _configuration=None):  # noqa: E501
        """SlackProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._email = None
        self._channel_id = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if email is not None:
            self.email = email
        if channel_id is not None:
            self.channel_id = channel_id

    @property
    def access_token(self):
        """Gets the access_token of this SlackProfile.  # noqa: E501


        :return: The access_token of this SlackProfile.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SlackProfile.


        :param access_token: The access_token of this SlackProfile.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def email(self):
        """Gets the email of this SlackProfile.  # noqa: E501


        :return: The email of this SlackProfile.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SlackProfile.


        :param email: The email of this SlackProfile.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def channel_id(self):
        """Gets the channel_id of this SlackProfile.  # noqa: E501


        :return: The channel_id of this SlackProfile.  # noqa: E501
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this SlackProfile.


        :param channel_id: The channel_id of this SlackProfile.  # noqa: E501
        :type: str
        """

        self._channel_id = channel_id

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
        if issubclass(SlackProfile, dict):
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
        if not isinstance(other, SlackProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlackProfile):
            return True

        return self.to_dict() != other.to_dict()
