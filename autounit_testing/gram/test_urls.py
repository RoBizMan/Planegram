from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Gram, Aircraft
import datetime


class GramUrlsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.aircraft = Aircraft.objects.create(
            plane_make="Boeing", plane_model="747"
        )
        self.gram = Gram.objects.create(
            caption="Test Gram",
            image="placeholder",
            plane=self.aircraft,
            date_photographed=datetime.date.today(),
            photographer=self.user
        )
        self.client.login(
            username='testuser', password='testpass'
        )  # Log in the user

    def test_grams_url_resolves(self):
        url = reverse('grams')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gram_detail_url_resolves(self):
        url = reverse(
            'gram_detail', args=[self.gram.pk]
        )  # Use the test gram's pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gram_action_url_resolves(self):
        url = reverse(
            'gram_action', args=[self.gram.pk]
        )  # Use the test gram's pk
        response = self.client.post(
            url, {'action': 'like'}
        )  # Simulate a like action
        self.assertEqual(response.status_code, 302)  # Should redirect

    def test_edit_gram_url_resolves(self):
        url = reverse(
            'edit_gram', args=[self.gram.pk]
        )  # Use the test gram's pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_report_gram_url_resolves(self):
        # Create a different user for reporting
        reporter = User.objects.create_user(
            username='reporter', password='reportpass'
        )

        # Log in the reporter
        self.client.login(username='reporter', password='reportpass')

        url = reverse(
            'report_gram', args=[self.gram.pk]
        )  # Use the test gram's pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Now it should return 200
