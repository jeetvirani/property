"""
A module which contains utilities for test cases
"""
# pylint: disable=too-few-public-methods
import json

from django.core.management import call_command
from django.test import Client

from property.authentication.constants import FORGOT_PASSWORD_EXPIRY_TIME
from property.services.jwt_utils import JWT_UTIL


class MockTestUtils:
    """
    A class which is used for mocking
    """
    def __init__(self):
        pass


MOCK_TEST_UTILS = MockTestUtils()


def get_jwt(payload):
    """
    Provides JWT for given payload
    :param payload:
    :return: JWT
    """
    return JWT_UTIL.encode(payload=payload, expiry_time=FORGOT_PASSWORD_EXPIRY_TIME)


def load_test_data(fixture_data):
    """
    load fictures for test cases
    :return:
    """
    call_command('loaddata', fixture_data, verbosity=0)


def get_token(username, password):
    """
    get login token for the user
    :param user_name:
    :param password:
    :return:
    """
    payload = dict(password=password, username=username)
    data = json.dumps(payload)
    client = Client()
    resp = client.post('/auth/login/', data=data, content_type='application/json')
    login_data = json.loads(resp.content.decode('utf-8'))
    login_token = 'TOKEN ' + login_data['token']
    return login_token