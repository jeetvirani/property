"""
A module for authentication serializers
"""
from rest_framework import serializers

from property.authentication.constants import MIN_PASSWORD_LENGTH, \
    WEAK_PASSWORD


class BaseSerializer(serializers.Serializer):
    """
    Base Serializer which overrides create and update methods
    """
    def create(self, validated_data):
        """
        Overriding BaseClass method
        :param validated_data:
        :return:
        """
        pass

    def update(self, instance, validated_data):
        """
        Overriding BaseClass method
        :param instance:
        :param validated_data:
        :return:
        """
        pass


class LoginValidator(BaseSerializer):
    """
    a serializer to serialize and validate username and password
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class EmailValidator(BaseSerializer):
    """
    a serializer to validate Email
    """
    email = serializers.EmailField(required=True)


class PasswordValidator(BaseSerializer):
    """
    a serializer to validate password
    """
    password = serializers.CharField(required=True)

    @staticmethod
    def validate_password(password):
        """
        Validates the password to satisfy a length of atleast 8 and to be a alphanumeric Character,
        else raises validation error.
        :return:
        """
        if len(password) < MIN_PASSWORD_LENGTH or password.isalpha() or password.isnumeric():
            raise serializers.ValidationError(WEAK_PASSWORD)

        return password


class SignUpValidator(PasswordValidator):
    """
    a serializer for SignUp
    """
    mobile_no = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

