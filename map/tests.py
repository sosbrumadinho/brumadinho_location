from django.test import TestCase, Client
from django.urls import reverse


class TestFrontEnd(TestCase):
    def setUp(self):
        self.c = Client()
        self.response = self.c.get(reverse('map:map'))

    def test_endpoint_result(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed('index.html')
