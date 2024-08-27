from django.test import TestCase
from .forms import ReportForm
from blog.models import Report, Gram, Aircraft
from django.contrib.auth.models import User
import datetime

class ReportFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.aircraft = Aircraft.objects.create(plane_make="Boeing", plane_model="747")
        self.gram = Gram.objects.create(
            caption="Test Gram",
            image="placeholder",
            plane=self.aircraft,
            date_photographed=datetime.date.today(),
            photographer=self.user
        )

    def test_report_form_valid(self):
        form_data = {'message': 'This is a test report.'}
        form = ReportForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_report_form_invalid_empty_message(self):
        form_data = {'message': ''}
        form = ReportForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)

    def test_report_form_invalid_long_message(self):
        form_data = {'message': 'x' * 301}
        form = ReportForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)