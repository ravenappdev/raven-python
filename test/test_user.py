# coding: utf-8

"""
    Raven API

    This is OpenAPI defintion for the APIs of Raven.  You can find out more about Raven at [https://ravenapp.dev/](https://ravenapp.dev/).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@ravenapp.dev
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import raven
from raven.models.user import User  # noqa: E501
from raven.exceptions.rest import RavenException


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """Test User"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.user.User()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
