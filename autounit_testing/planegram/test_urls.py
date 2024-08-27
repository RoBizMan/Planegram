from django.test import TestCase


class PlanegramUrlsTest(TestCase):
    def test_home_url_resolves(self):
        response = self.client.get('/')  # Access the root URL directly
        self.assertEqual(response.status_code, 200)

    def test_404_handler(self):
        response = self.client.get(
            '/non-existent-page/'
        )  # Access a non-existent URL
        self.assertEqual(
            response.status_code, 404
        )  # Should trigger the 404 handler

    def test_500_handler(self):
        response = self.client.get(
            '/error/'
        )  # Access the error view
        self.assertEqual(
            response.status_code, 500
        )  # Should trigger the 500 handler
