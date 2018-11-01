"""
A module Which serves SignUp API
"""
import json

from django.http import JsonResponse
from django.views import View

from property.authentication.serializers import SignUpValidator
from property.authentication.utils import catch_error
from property.pms.models import User
from property.services.jwt_utils import JWT_UTIL
from property.services.utils import validate_serializer, generate_user_token
from property.services.exceptions import BadToken, UserNotFound, UserIsActive


class SignUp(View):
    """
    A class which has post method for reset password functionality
    """
    @catch_error
    def post(self, request, token):
        """
        This method will take the jwt token and first_name, last_name and password in body and
        validates and sets the attribute to the user object password of the user. It will raise
        BadToken, ValueError, UserNotFound and JWT Errors when in appropriate data is passed.
        :param request:
        :param token:
        :return: JsonResponse
        """

        data = json.loads(request.body.decode('utf-8'))

        serializer = SignUpValidator(data=data)
        validate_serializer(serializer)

        payload = JWT_UTIL.decode(token)
        uuid = payload.get('uuid')
        if not uuid:
            raise BadToken

        try:
            user = User.objects.get(uuid=uuid)
        except Exception:
            raise UserNotFound

        if user.is_active:
            raise UserIsActive

        password = serializer.validated_data['password']

        for key, value in serializer.validated_data.items():
            setattr(user, key, value)

        user.set_password(password)
        user.verify(True)
        user.set_state(True)

        token = generate_user_token(user)


        data = dict(
            error=False,
            msg='Successful',
            token=token,
            user=user.full_name
        )

        return JsonResponse(data)
