from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from listings.models import MissingPerson


class TestListingsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.time = timezone.now()
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.comm')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user)
    
    def test_listings_all_page(self):
        response = self.client.get(reverse('listings:listings_all'))
        self.assertEqual(response.status_code, 200)

    def test_listings_detail_page(self):
        response = self.client.get(reverse('listings:detail', args=[0]))
        self.assertEqual(response.status_code, 200)

    def test_listings_search_page(self):
        response = self.client.get(
            reverse('listings:search'), {
                'city': 'test',
                'state': 'test',
                'sex': 'test',
                'start_year': 2000,
                'end_year': 2010
            }
        )
        self.assertEqual(response.status_code, 200)
