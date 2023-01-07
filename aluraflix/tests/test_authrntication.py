from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    user_name = 'Anakin'
    password = '123'

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user(self.user_name, password=self.user_name)

    def test_user_with_correct_credentials(self):
        self.user = authenticate(username=self.user_name, password=self.user_name)

        self.assertTrue((self.user is not None) and self.user.is_authenticated)

    def test_GET_request_not_authorized(self):
        response = self.client.get(self.list_url)
        self.assertAlmostEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_reqyest_get_authorization(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
