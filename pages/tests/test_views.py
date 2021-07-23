from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from listings.models import MissingPerson
from requestors.models import Requestor


class TestPagesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.time = timezone.now()
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.comm')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user)
        Requestor.objects.create(name='test', photo='test', user=self.user)

    def test_index_page(self):
        response = self.client.get(reverse('pages:index'))
        self.assertEqual(response.status_code, 200)

    def test_map_page(self):
        response = self.client.get(
            reverse('pages:map'), {
                'city': 'test',
                'state': 'test',
            }, xhr=True
        )
        self.assertEqual(response.status_code, 200)
    
    def get_client_of_request_page(self, client, fail=False):
        state = 'stateless' if fail else 'state'
        response = client.post(
            reverse('pages:request'), {
                'name': 'test',
                'sex': 'M',
                'age': 20,
                'city': 'test',
                state: 'test',
                'address': 'test',
                'date': timezone.now(),
                'description': 'test'
            }
        )

        return response

    def test_request_page_success(self):
        client = self.client
        client.force_login(self.user)
        response = self.get_client_of_request_page(client)
        self.assertEqual(response.status_code, 200)

    def test_request_page_fail(self):
        client = self.client
        client.force_login(self.user)
        response = self.get_client_of_request_page(client, fail=True)
        self.assertEqual(response.status_code, 200)
