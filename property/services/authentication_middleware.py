"""
A Module to authenticate the every rest request.
"""
from rest_framework import authentication
from rest_framework import exceptions

from property.models import User

from property.settings import LOGIN_TTL


class RedisTokenExpiryAuthentication(authentication.BaseAuthentication):
    """
    A middleware through which every rest request will pass through.
    """
    def authenticate(self, request):
        """
        This will verify whether the request is authenticated or not. On having a valid token in
        redis this will reset the TTL of the token and returns the user object. On un-existing
        user and token returns 401.
        :param request
        :return: tuple(user, None)
        """
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if not auth_header:
            raise exceptions.AuthenticationFailed('No token provided')

        auth_header = auth_header.split()

        if auth_header[0].lower() != 'token':
            raise exceptions.AuthenticationFailed('Invalid Token Provided')

        token = auth_header[1]
         #TODO Token validation
        user_id = request.user


        if not user_id:
            raise exceptions.AuthenticationFailed('Token Expired')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is not active')

        return user, None

    def authenticate_header(self, request):
        """
        Sets WWW-Authenticate header value and responds with 401.
        :param request:
        :return: WWW-Authenticate header value
        """
        return "Token"
