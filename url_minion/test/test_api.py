from django.conf import settings
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class ApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_short_url_201(self):
        response = self.client.post(f'/shorten_url/', data=dict(url='http://test.com'))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['shortened_url'], f'{settings.APP_URL}/867nv')
        
    def test_create_short_url_no_schema(self):
        response = self.client.post(f'/shorten_url/', data=dict(url='test.com'))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['shortened_url'], f'{settings.APP_URL}/867nv')
        
    def test_create_bad_url(self):
        response = self.client.post(f'/shorten_url/', data=dict(url='http://test.c'))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_short_url_redirect(self):
        long_url = 'http://test.com'

        self.client.post(f'/shorten_url/', data=dict(url='test.com'))

        response = self.client.get(f'/867nv/')

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, long_url)

    def test_short_url_redirect_404(self):
        long_url = 'http://test.com'
        response = self.client.get(f'/nbvhfgctryfu/', data=dict(url=long_url))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
