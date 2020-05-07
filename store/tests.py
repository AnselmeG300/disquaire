from django.urls import reverse
from django.test import TestCase

# Create your tests here.
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)