from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Gram, Aircraft
import datetime
from upload.test_urls import UploadUrlsTest


class UploadGramViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.aircraft = Aircraft.objects.create(
            plane_make="Boeing", plane_model="747"
        )
        self.client.login(username='testuser', password='testpass')

    def test_upload_gram_view_get(self):
        response = self.client.get(reverse('upload'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'upload/upload.html'
        )  # Ensure the correct template is used

    def test_upload_gram_view_post_valid(self):
        form_data = {
            'date_photographed': datetime.date.today(),
            'caption': 'Test Caption',
            'image': '',
            'plane': self.aircraft.pk,
        }
        response = self.client.post(reverse('upload'), data=form_data)
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect after successful upload
        self.assertTrue(Gram.objects.filter(
            caption='Test Caption').exists()
        )  # Check if the Gram was created

    def test_upload_gram_view_post_invalid(self):
        form_data = {
            'date_photographed': datetime.date.today(),
            'caption': '',
            'image': '',
            'plane': self.aircraft.pk,
        }
        response = self.client.post(reverse('upload'), data=form_data)
        self.assertEqual(
            response.status_code, 200
        )  # Should return to the form with errors
        self.assertFormError(
            response, 'form', 'caption', 'This field is required.'
        )  # Check for specific error
