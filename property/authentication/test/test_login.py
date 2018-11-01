"""
Unit Test for Login module
"""
import json

from django.test import TestCase

from property.authentication.test.test_utilities import login_test_data


class LoginTest(TestCase):
    """
    TestCases for Login API
    """
    def setUp(self):
        login_test_data()

    def call_api(self, payload):
        """
        Take payload and calls the api with data.
        :param payload:
        :return: status, data
        """

        data = json.dumps(payload)
        resp = self.client.post('/api/auth/login/', data=data, content_type='application/json')
        return resp.status_code, json.loads(resp.content.decode('utf-8'))

    def test_login_success(self):
        """
        Test case to test Successful Login.
        :return:
        """
        payload = dict(password='test_password',email='test_user@testing.com')
        status_code, data = self.call_api(payload=payload)

        self.assertEqual(status_code, 200)
        self.assertEqual('token' in data, True)

    def test_bad_request(self):
        """
        Test case to test bad request by not passing a parameter.
        :return:
        """
        payload = dict(password='wrong_password')
        status_code, data = self.call_api(payload=payload)

        self.assertEqual(status_code, 400)
        self.assertEqual(data['detail'], 'Invalid Parameter passed')

    def test_login_invalid_username(self):
        """
        Test case to test Invalid Username
        :return:
        """
        payload = dict(email='aaaa@testinh.com', password='test_password')
        status_code, data = self.call_api(payload=payload)

        self.assertEqual(status_code, 401)
        self.assertEqual(data['detail'], 'Invalid Username or Password')

    def test_login_invalid_password(self):
        """
        Test case to test Invalid Password.
        :return:
        """
        payload = dict(email='test_user@testing.com', password='wrong_password')
        status_code, data = self.call_api(payload=payload)

        self.assertEqual(status_code, 401)
        self.assertEqual(data['detail'], 'Invalid Username or Password')
