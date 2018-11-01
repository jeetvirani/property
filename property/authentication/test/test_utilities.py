"""
A module which has all the test case utilities.
"""
from property.pms.models import User


def login_test_data():
    """
    A function which creates test data for login api
    :return:
    """
    user = User.objects.create(email='test_user@testing.com')
    user.set_password('test_password')
    user.save()

    return user


def forgot_password_test_data():
    """
    A function which creates test data for forgot password
    :return:
    """
    user = User.objects.create(email='test_email_1@testing.com')
    user.set_password('test_password')
    user.is_active = True
    user.save()

def in_active_user():
    """
    A function which creates test data for forgot password
    :return:
    """
    user = User.objects.create(email='test_email_2@testing.com')
    user.set_password('test_password')
    user.is_active = False
    user.save()
