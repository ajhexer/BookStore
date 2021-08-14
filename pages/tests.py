from django.test import SimpleTestCase
from django.urls import reverse


class AboutPageTests(SimpleTestCase): # new
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

