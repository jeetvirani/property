"""
A module which contains utils function
"""
import logging
from functools import wraps

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response


from property.services.exceptions import InvalidUsernameOrPassword, UserNotActive


LOGGER = logging.getLogger('property')

INTERNAL_SERVER_ERROR = "Internal Server Error. Please retry after some time."


def validate_serializer(serializer):
    """
    To validate a serializer and raise error on bad validation
    :param serializer:
    :return:
    """
    if not serializer.is_valid():
        raise ValueError(serializer.errors)


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
