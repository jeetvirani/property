"""
A module which contains all the custom exceptions
"""
from abc import abstractmethod


class CustomException(Exception):
    """
    A Abstract Base Exception Class.
    """
    @property
    @abstractmethod
    def message(self):
        """
        A property which has to be assigned on creating a custom exceptions.
        :return:
        """
        pass

    def __str__(self):
        return self.message


class InvalidUsernameOrPassword(CustomException):
    """
    This will raise when username or password is wrong.
    """
    message = 'Invalid Username or Password'


class UserNotActive(CustomException):
    """
    This will raise when user is not active.
    """
    message = 'User is not active'



class UserNotFound(CustomException):
    """
    This will be raised when user is not found in DB
    """
    message = 'User not Found'


class BadToken(CustomException):
    """
    This will be raised when Invalid Token is passed
    """
    message = 'Invalid Token'


class UserIsActive(CustomException):
    """
    This will be raised when User is active
    """
    message = 'User is active'
