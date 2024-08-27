from django.test import TestCase
from django.urls import reverse


class UploadUrlsTest(TestCase):
    def test_upload_url_resolves(self):
        url = reverse('upload')
        self.assertEqual(url, '/upload/')
