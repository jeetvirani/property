"""
A module for authentication serializers
"""
from rest_framework import serializers


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

