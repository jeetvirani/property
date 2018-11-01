"""
A module which contains utils function
"""
import hashlib
import time
import logging
from datetime import timedelta
from functools import wraps
from django.utils import timezone

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response


from property.services.exceptions import InvalidUsernameOrPassword, UserNotActive


LOGGER = logging.getLogger('property')

INTERNAL_SERVER_ERROR = "Internal Server Error. Please retry after some time."


def get_absolute_time(expiry_time=0):
    """
    This Function will return the absolute time by adding expiry_time seconds to current time.
    :param expiry_time:
    :return:
    """
    current_date = timezone.localtime()
    delta = timedelta(seconds=expiry_time)
    fmt = '%Y-%m-%d %H:%M %Z'
    actual_time = current_date + delta
    return actual_time.strftime(fmt)


def generate_user_token(user):
    """
    This function generates the token by applying md5 on hash of pk and time.
    :param user:
    :return: token
    """
    order = hash((user.pk, time.time()))
    encoded_order = str(order).encode('utf-8')
    token = hashlib.md5(encoded_order).hexdigest()
    return token


def validate_serializer(serializer):
    """
    To validate a serializer and raise error on bad validation
    :param serializer:
    :return:
    """
    if not serializer.is_valid():
        raise ValueError("Invalid Parameter passed")


def rollback_log_error(error, status_code):
    """
    To log error
    :param error:
    :param status_code:
    :return:
    """
    transaction.set_rollback(True)
    error = "Error {0}, {1}".format(status_code, str(error))
    LOGGER.error(error)
    error = dict(detail=str(error))
    return Response(error, status=status_code)


def catch_error(api_function):
    """
    A decorator used to catch an exceptions.
    :param api_function:
    :return:
    """
    @wraps(api_function)
    def inner_fn(*args, **kwargs):
        """
        Wraps a function with exceptions.
        :param args:
        :param kwargs:
        :return:
        """
        with transaction.atomic():
            try:

                return api_function(*args, **kwargs)

            except InvalidUsernameOrPassword as err:
                return rollback_log_error(err, status_code=status.HTTP_401_UNAUTHORIZED)

            except UserNotActive as err:
                return rollback_log_error(err, status_code=status.HTTP_403_FORBIDDEN)

            except ValueError as err:
                return rollback_log_error(err, status_code=status.HTTP_400_BAD_REQUEST)

            except Exception as err:
                return rollback_log_error(err, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return inner_fn
