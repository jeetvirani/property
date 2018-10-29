# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class BaseModel(models.Model):
    """
    A Base model which provides timestamps, active and deleted information
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class PropertyInterest(models.Model):
    property_interest_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'property_interest'

class PropertyType(models.Model):
    property_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'property_type'

class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'user_type'

class User(AbstractUser, BaseModel):
    """
    A model which overrides User model
    """
    interest = models.ManyToManyField(PropertyInterest, related_name='interest')
    property_type = models.ManyToManyField(PropertyType, related_name='property_type')
    app = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_contract_info = models.CharField(max_length=50)
    company_profile = models.CharField(max_length=50)
    user_type = models.ManyToManyField(UserType, related_name='user_type')



