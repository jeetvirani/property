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
    def post(self, request):
        """
        This method will take the jwt token and first_name, last_name and password in body and
        validates and sets the attribute to the user object password of the user. It will raise
        BadToken, ValueError, UserNotFound and JWT Errors when in appropriate data is passed.
        :param request:
        :param token:
        :return: JsonResponse
        """

        data = json.loads(request.body.decode('utf-8'))
        # print(data)
        # serializer = SignUpValidator(data=data)
        # validate_serializer(serializer)
        # print(serializer)
        print(data['username'])
        User.objects.create(
            username=data['username'],
            mobile_no=data['mobile_no']
        )
        print(User)
        # user.set_password(data['password'])
        # user.save()
        
        # password = serializer.validated_data['password']
        # for key, value in serializer.validated_data.items():
        #     setattr(User, key, value)

        # data = dict(
        #     error=False,
        #     msg='Successful',
        # )

        return JsonResponse("jeet")
