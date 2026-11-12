from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
class AccountTests(TestCase):
    def test_registration_creates_profile_and_logs_in(self):
        response=self.client.post(reverse('register'),{'username':'learner1','email':'learner@example.com','password1':'StrongPass!482','password2':'StrongPass!482'})
        self.assertRedirects(response,reverse('dashboard'))
        user=User.objects.get(username='learner1')
        self.assertTrue(user.profile)
        self.assertTrue('_auth_user_id' in self.client.session)
