"""
A module which will register the models on Django Admin
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from property.pms.models import User, Property, PropertyInterest, PropertyType, UserType, \
    NearBy, Location, Amenities, Document, TransactionType, UnitArea, Booking


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Defining admin model for custom User model with no username field.
    """

    fieldsets = (
        (None, {'fields': ('username','email', 'password',)}),
        # (_('Profile'), {'fields': ('is_verified',)}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        # (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_deleted',
        #                                'groups', 'user_permissions')}),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('username','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username','email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(Property)
admin.site.register(PropertyInterest)
admin.site.register(PropertyType)
admin.site.register(UserType)
admin.site.register(NearBy)
admin.site.register(Location)
admin.site.register(Amenities)
admin.site.register(Document)
admin.site.register(TransactionType)
admin.site.register(UnitArea)
admin.site.register(Booking)
