# -*- coding: utf-8 -*-
import os
import unittest

from dotenv import load_dotenv

from auth0plus.oauth import get_token


load_dotenv('.env')
skip = int(os.getenv('SKIP_INTEGRATION_TESTS', 1))


class TestGetAToken(unittest.TestCase):
    @unittest.skipIf(skip, 'SKIP_INTEGRATION_TESTS==1')
    def setUp(self):
        """
        Get a non-interactive client secret
        """
        self.domain = os.getenv('DOMAIN')
        self.client_id = os.getenv('CLIENT_ID')
        self.secret_id = os.getenv('CLIENT_SECRET')

    def test_get_a_token(self):
        """
        Test getting a 24 hour token from the oauth token endpoint
        """
        token = get_token(self.domain, self.client_id, self.secret_id)
        assert token['access_token']



