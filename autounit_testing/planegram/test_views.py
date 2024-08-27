from django.test import TestCase

class PlanegramViewsTest(TestCase):
    def test_handler404(self):
        response = self.client.get('/non-existent-page/')  # Access a non-existent URL
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')  # Ensure the correct template is used

    def test_handler500(self):
        response = self.client.get('/error/')  # Access the error view
        self.assertEqual(response.status_code, 500)  # Should trigger the 500 handler
        self.assertTemplateUsed(response, 'errors/500.html')  # Ensure the correct template is used
