from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class ApiViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.client = APIClient()

        self.position_data = {'lat': -20.135896, 'lng': -44.123509}
        self.expected_result = {'lat': -20.152766, 'lng': -44.127033}
        self.response = self.client.post(
            reverse('api:coordinate_calculate'),
            self.position_data,
            format="json")

    def test_api_can_return_response(self):
        """Test the api has response capability."""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_get_not_allowed(self):
        """Test that the api don't return get method"""
        new_client = APIClient()
        res = new_client.get(
            reverse('api:coordinate_calculate'), format="json")
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_api_return_expected_values(self):
        """Test the api can return expected json data."""

        self.assertEquals(self.response.data, self.expected_result)
