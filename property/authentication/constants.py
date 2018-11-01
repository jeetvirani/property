"""
Constants for authentication module
"""
from property.settings import FRONT_END_URL

MIN_PASSWORD_LENGTH = 8

WEAK_PASSWORD = "Weak Password. Make Sure it contains minimum 8 Characters, 1 Alphabet, 1 Number " \
                "and 1 special Character."

FORGOT_PASSWORD_EXPIRY_TIME = 60*60

FORGOT_PASSWORD_EMAIL_TEMPLATE = '3986455dc581a9b89ea6601ce787278b'

RESET_PASSWORD_END_POINT = FRONT_END_URL + '/reset-password/{0}/'

SIGNUP_EXPIRY_TIME = 24*60*60

SIGNUP_TEMPLATE = '934b67ff06f9568ff6739650e1527bea'

SIGN_UP_END_POINT = FRONT_END_URL + '/signup/{0}'

NOTIFICATION_TEMPLATE = 'a2478706-b173-466f-9ad6-62da6bd651c7'

REDIS_FORGOT_PWD_TAG = 'forgot_pwd_{0}'
