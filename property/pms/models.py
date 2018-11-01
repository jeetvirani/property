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
    user_id = models.AutoField(primary_key=True)
    interest = models.ManyToManyField(PropertyInterest, related_name='interest')
    property_type = models.ManyToManyField(PropertyType, related_name='property_type')
    app = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_contract_info = models.CharField(max_length=50)
    company_profile = models.CharField(max_length=50)
    user_type = models.ManyToManyField(UserType, related_name='user_type')
    class Meta:
        db_table = 'user' 

class NearBy(models.Model):
    nearby_Id = models.AutoField(primary_key=True)
    landmark = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    railway = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    class Meta:
        db_table = 'near_by'

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    society = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longiture = models.CharField(max_length=50)
    class Meta:
        db_table = 'location'  

class Amenities(models.Model):
    amenity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'amenities'  

class Document(models.Model):
    doc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    class Meta:
        db_table = 'document'    

class TransactionType(models.Model):
    trans_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'transaction_type' 

class UnitArea(models.Model):
    unit_area_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'unit_area'         

class Property(BaseModel):
    property_id = models.AutoField(primary_key=True)
    nearby = models.ManyToManyField(NearBy, related_name='near_by')
    location = models.ManyToManyField(Location, related_name='location')
    amenity = models.ManyToManyField(Amenities, related_name='amenities')
    document = models.ManyToManyField(Document, related_name='document')
    transaction_type = models.ManyToManyField(TransactionType, related_name='transaction_type')
    property_type = models.ManyToManyField(PropertyType, related_name='property_type')
    unit_area = models.ManyToManyField(UnitArea, related_name='unit_area')
    budget = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    bedrooms = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    bathrooms = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    furnished = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    no_of_floors = models.CharField(max_length=50)
    no_of_carparking = models.CharField(max_length=50)
    posted_by = models.CharField(max_length=50)
    no_of_floors = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    builtup_area = models.CharField(max_length=50)
    land_area = models.CharField(max_length=50)
    carpet_area = models.CharField(max_length=50)
    is_buyable = models.BooleanField(default=False)
    user_type = models.ManyToManyField(UserType, related_name='Property_user_type')
    class Meta:
        db_table = 'property' 


class Booking(BaseModel):
    booking_id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User, related_name='user')
    property = models.ManyToManyField(Property, related_name='property')
    seller = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    class Meta:
        db_table = 'booking'
  
