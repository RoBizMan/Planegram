from django.urls import reverse
from django.test import TestCase

class BlogUrlsTest(TestCase):
    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)