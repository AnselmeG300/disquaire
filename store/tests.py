from django.urls import reverse
from django.test import TestCase

# Create your tests here.
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

from .models import Album, Artist, Contact, Booking

class DetailPageTestCase(TestCase):

    # test that detail page returns a 200 if the item exists.
    def test_detail_page_returns_200(self):
        impossible = Album.objects.create(title="Transmission Impossible")
        album_id = Album.objects.get(title='Transmission Impossible').id
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_returns_404(self):
        impossible = Album.objects.create(title="Transmission Impossible")
        album_id = Album.objects.get(title='Transmission Impossible').id + 1
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)