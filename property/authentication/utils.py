"""
A module which has utilities for authentication
"""
import json
import logging
from functools import wraps

from django.db import transaction
from django.http import JsonResponse
from django.test import TestCase
from rest_framework import status


LOGGER = logging.getLogger('property')


def catch_error(api_function):
    """
    A decorator function which captures errors for Django API.
    :param api_function:
    :return: decorated function.
    """
    @wraps(api_function)
    def inner_fn(*args, **kwargs):
        """
        A Function which wraps the provided function with exception blocks and it's status.
        :param args:
        :param kwargs:
        :return:
        """
        with transaction.atomic():
            try:
                return api_function(*args, **kwargs)
            except ValueError as err:
                return rollback_log_error(err, status_code=status.HTTP_400_BAD_REQUEST)

            except Exception as err:
                return rollback_log_error(err, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return inner_fn


def rollback_log_error(err, status_code):
    """
    A function which will take error and status code, logs the error and returns JsonResponse.
    :param err:
    :param status_code:
    :return: JsonResponse
    """
    transaction.set_rollback(True)
    error = "Error {0}, {1}".format(status_code, str(err))
    LOGGER.error(error)
    error = dict(detail=str(err))
    return JsonResponse(error, status=status_code)


class BaseTestCase(TestCase):
    """
    A Base Class for TestCases
    """
    def call_post_api(self, url, payload):
        """
        A method which takes url and payload and calls with post.
        :param url:
        :param payload:
        :return:
        """
        data = self.json_dumps(payload)
        resp = self.client.post(url, data=data, content_type='application/json')
        return resp.status_code, json.loads(resp.content.decode('utf-8'))

    def call_get_api(self, url):
        """
        A method which takes payload and calls with get.
        :param url:
        :return:
        """
        resp = self.client.get(url, content_type='application/json')
        return resp.status_code, json.loads(resp.content.decode('utf-8'))

    def json_dumps(self, payload):
        """
        A method which dumps the data
        :param payload:
        :return:
        """
        return json.dumps(payload)
