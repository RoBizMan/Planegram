from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Gram, Report, Aircraft
import datetime


class GramViewsTest(TestCase):
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
        )  # Ensure user is logged in

    def test_grams_list_view(self):
        response = self.client.get(reverse('grams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gram/grams_list.html')

    def test_gram_detail_view(self):
        response = self.client.get(reverse('gram_detail', args=[self.gram.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gram/gram_detail.html')

    def test_report_gram_view(self):
        # Create a different user for reporting
        reporter = User.objects.create_user(
            username='reporter', password='reportpass'
        )

        # Log in the reporter
        self.client.login(username='reporter', password='reportpass')

        response = self.client.get(reverse('report_gram', args=[self.gram.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gram/report_gram.html')

    def test_report_gram_submission(self):
        # Create a different user for reporting
        reporter = User.objects.create_user(
            username='reporter', password='reportpass'
        )

        # Log in the reporter
        self.client.login(username='reporter', password='reportpass')

        # Submit the report
        response = self.client.post(
            reverse('report_gram', args=[self.gram.pk]),
            {'message': 'Inappropriate content'}
        )

        # Check for a redirect after submission
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertTrue(
            Report.objects.filter(gram=self.gram, user=reporter).exists()
        )  # Check if report was created

    def test_gram_action_like(self):
        response = self.client.post(
            reverse('gram_action', args=[self.gram.pk]), {'action': 'like'}
        )
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertIn(
            self.user, self.gram.love.all()
        )  # Check if user liked the gram

    def test_gram_action_delete(self):
        response = self.client.post(
            reverse('gram_action', args=[self.gram.pk]), {'action': 'delete'}
        )
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertFalse(
            Gram.objects.filter(pk=self.gram.pk).exists()
        )  # Check if the gram was deleted
