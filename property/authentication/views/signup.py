"""
A module Which serves SignUp API
"""
import json

from django.http import JsonResponse
from django.views import View

from property.authentication.serializers import SignUpValidator
from property.authentication.utils import catch_error
from property.pms.models import User
from property.services.utils import validate_serializer


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
        serializer = SignUpValidator(data=data)
        validate_serializer(serializer)
        # print(serializer)
        password = serializer.validated_data['password']
        for key, value in serializer.validated_data.items():
            setattr(User, key, value)
        user = User.objects.create(
            username=data['username'],
            password=password,
            mobile_no=data['mobile_no']
        )
        user.save()

        return JsonResponse({"suc": True})
