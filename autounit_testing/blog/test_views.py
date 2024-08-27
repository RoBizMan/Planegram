from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class HomepageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
            )

    def test_homepage_view_anonymous_user(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_homepage_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('homepage'))
        self.assertRedirects(response, reverse('grams'))
