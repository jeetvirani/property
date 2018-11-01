"""
A module for performing JWT Operations
"""

from datetime import datetime, timedelta

import jwt

from property.settings import JWT_SECRET, ENCODING_ALGORITHM, JWT_EXP_DELTA_SECONDS



class JwtUtils:
    """
    A class which contains JWT Operations
    """
    secret = JWT_SECRET
    algorithm = ENCODING_ALGORITHM
    expiry_time = JWT_EXP_DELTA_SECONDS

    def encode(self, payload, expiry_time=expiry_time):
        """

        :param payload:
        :param expiry_time:
        :return:
        """
        payload['exp'] = datetime.utcnow() + timedelta(seconds=expiry_time)
        encoded = jwt.encode(payload, self.secret, algorithm=self.algorithm)
        token = encoded.decode('utf-8')
        return token

    def decode(self, encoded):
        """
        A method to decode data
        :param encoded:
        :return: payload
        """
        payload = jwt.decode(encoded, self.secret, algorithms=[self.algorithm], verify=True)
        return payload


JWT_UTIL = JwtUtils()
