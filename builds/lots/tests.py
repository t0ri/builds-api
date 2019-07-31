from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class AccountsTest(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new lot.
        """
        data = {
            'title': 'asdf',
            'description': 'asdf',
            'gallery': 'asdf',
            'lot_type': 'asdf',
            'bedrooms': 'asd',
            'bathrooms': 'asd',
            'sims': 'asd',
            'packs': 'adf'
        }
        self.create_url = reverse('sign-up')
        response = self.client.post(self.create_url, data, 'json')
        # We want to make sure we have 1 user in the database..
        self.assertEqual(User.objects.count(), 1)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)