from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from contacts.models import Contact
from listings.models import MissingPerson


class TestContactsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.time = timezone.now()
        self.user1 = User.objects.create(id=0, username='test1', password='test1', email='test1@test.com')
        self.user2 = User.objects.create(id=1, username='test2', password='test2', email='test2@test.com')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user1)
        self.contact = Contact.objects.create(from_name='test', missing_person=self.missing_person, email='test@test.com', phone=123456789,
                                              message='test', last_seen=self.time, contact_date=self.time, user=self.user1)

    def get_client_of_contact_page(self, client, user_id):
        response = client.post(
            reverse('contacts:contact'), {
                'missing_person_id': 0,
                'name': 'test',
                'phone': 123456789,
                'message': 'test',
                'user_id': user_id,
                'requestor_email': 'test@test.com',
                'date': self.time
        })

        return response

    def test_contact_page_success(self):
        client =  self.client
        client.force_login(self.user2)

        response = self.get_client_of_contact_page(client, self.user2.id)

        self.assertEqual(response.status_code, 302)

    def test_contact_page_fail(self):
        client =  self.client
        client.force_login(self.user1)

        response = self.get_client_of_contact_page(client, self.user1.id)

        self.assertEqual(response.status_code, 302)
