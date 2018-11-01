"""
A module which has logic for authentication
"""
import json

from django.http import JsonResponse
from django.views import View
from rest_framework.compat import authenticate

from property.authentication.serializers import LoginValidator
from property.authentication.utils import catch_error
from property.services.exceptions import InvalidUsernameOrPassword
from property.services.utils import generate_user_token, validate_serializer



class Login(View):
    """
    A class which has post method to authenticate
    """

    @catch_error
    def post(self, request):
        """
        A method used for login. upon getting username and password it will authenticate the user.
        if authentication returns None it will raise InvalidUsernamePassword Exception.if the
        details are valid it'll create a redis key with a TTL which will be sent back to user as
        a token along with data of organisations, applications, which belongs to user.
        :param request:
        :return: JsonResponse
        """
        data = json.loads(request.body.decode('utf-8'))

        serializer = LoginValidator(data=data)
        validate_serializer(serializer)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request=request, email=email, password=password)

        if not user:
            raise InvalidUsernameOrPassword

        token = generate_user_token(user)

        data = dict(
            error=False,
            msg='Successful',
            token=token,
            user=user.full_name,
            uuid=user.uuid
        )

        return JsonResponse(data)
