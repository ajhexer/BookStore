from django.test import TestCase
from django.contrib.auth import get_user_model


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

