from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from accounts.forms import CustomUserCreationForm

class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="ali",
            email='ali@yahoo.com',
            password='testpassword1234'
        )
        self.assertEqual(user.username, 'ali')
        self.assertEqual(user.email, 'ali@yahoo.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='ajhexer',
            email='ajhexer@yahoo.com',
            password='testpassword1234'
        )
        self.assertEqual(user.username, 'ajhexer')
        self.assertEqual(user.email, 'ajhexer@yahoo.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')



class SignupTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
    def test_signup_form(self):
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)