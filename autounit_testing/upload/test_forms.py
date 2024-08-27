from django.test import TestCase
from blog.models import Gram, Aircraft
from django.contrib.auth.models import User
from .forms import GramUpload
import datetime

class GramUploadFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.aircraft = Aircraft.objects.create(plane_make="Boeing", plane_model="747")

    def test_valid_form(self):
        form_data = {
            'date_photographed': datetime.date.today(),
            'caption': 'Test Caption',
            'image': '',  # Use an empty string instead of None
            'plane': self.aircraft.pk,
        }
        form = GramUpload(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_no_caption(self):
        form_data = {
            'date_photographed': datetime.date.today(),
            'caption': '',  # No caption provided
            'image': '',  # Use an empty string instead of None
            'plane': self.aircraft.pk,
        }
        form = GramUpload(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('caption', form.errors)

    def test_invalid_form_date_in_future(self):
        form_data = {
            'date_photographed': datetime.date.today() + datetime.timedelta(days=1),  # Future date
            'caption': 'Valid Caption',
            'image': '',  # Use an empty string instead of None
            'plane': self.aircraft.pk,
        }
        form = GramUpload(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Date photographed cannot be dated past today's date.", form.errors['__all__'])