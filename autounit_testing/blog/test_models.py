from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Aircraft, Gram, Report
import datetime

class AircraftModelTest(TestCase):
    def setUp(self):
        self.aircraft = Aircraft.objects.create(plane_make="Boeing", plane_model="747")

    def test_aircraft_str(self):
        self.assertEqual(str(self.aircraft), "Boeing | 747")

class GramModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='photographer', password='password')
        self.aircraft = Aircraft.objects.create(plane_make="Boeing", plane_model="747")
        self.gram = Gram.objects.create(
            caption="First Flight",
            image="placeholder",
            plane=self.aircraft,
            date_photographed=datetime.date.today(),
            photographer=self.user
        )

    def test_gram_str(self):
        self.assertEqual(str(self.gram), "First Flight by photographer")

    def test_future_date_validation(self):
        future_gram = Gram(
            caption="Future Flight",
            image="placeholder",
            plane=self.aircraft,
            date_photographed=datetime.date(2025, 1, 1),  # Future date
            photographer=self.user
        )
        with self.assertRaises(ValidationError):
            future_gram.full_clean()  # Use full_clean() to trigger validation

class ReportModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='reporter', password='password')
        self.aircraft = Aircraft.objects.create(plane_make="Boeing", plane_model="747")
        self.gram = Gram.objects.create(
            caption="First Flight",
            image="placeholder",
            plane=self.aircraft,
            date_photographed=datetime.date.today(),
            photographer=self.user
        )
        self.report = Report.objects.create(
            gram=self.gram,
            user=self.user,
            message="Inappropriate content"
        )

    def test_report_str(self):
        self.assertEqual(str(self.report), f"Report on {self.gram} submitted by {self.user}")