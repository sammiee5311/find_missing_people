from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from contacts.models import Contact
from listings.models import MissingPerson
from videos.models import ImagesFromVideo

from collections import defaultdict


class TestAccountViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.time = timezone.now()
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.comm')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user)
        self.contact = Contact.objects.create(from_name='test', missing_person=self.missing_person, email='test@test.com', phone=123456789,
                                              message='test', last_seen=self.time, contact_date=self.time, user=self.user)
        self.images_from_video = ImagesFromVideo.objects.create(id=0, name='test', photo='test', date=self.time, user=self.user,
                                                   missing_person=self.missing_person)

    def test_register_page_success(self):
        client = self.client
        response_register = client.post(reverse('accounts:register'), {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test1',
            'email': 'test@test.com',
            'password': 'TestTest123',
            'password_confirm': 'TestTest123'
        })

        uid = response_register.context['uid']
        token = response_register.context['token']
        response_email1 = client.post(reverse('accounts:activate', args=[uid, token]))
        response_email2 = client.post(reverse('accounts:activate', args=[uid, 'test']))

        self.assertEqual(response_register.context['user'].username, 'test1')
        self.assertEqual(response_email1.status_code, 302)
        self.assertEqual(response_email2.status_code, 200)
    
    def test_activate_page_invalid(self):
        response = self.client.get(reverse('accounts:activate', args=['test', 'test']))
        self.assertEqual(response.status_code, 200)

    def test_register_page_fail(self):
        client = self.client
        response = client.get(reverse('accounts:register'))

        self.assertIsNotNone(response.context['form'])

    def test_dashboard_page(self):
        client = self.client
        client.force_login(self.user)
        response = client.get(reverse('accounts:dashboard'))
        self.assertTupleEqual(response.context['images'][0][0], ('/media/test', 0))

    def test_dashboard_page_correct(self):
        client = self.client
        client.force_login(self.user)
        response = client.post(reverse('accounts:dashboard'), {
            'correct': '0,0',
        })
        self.assertDictEqual(response.context['images'], {})

    def test_dashboard_page_wrong(self):
        client = self.client
        client.force_login(self.user)
        response = client.post(reverse('accounts:dashboard'), {
            'wrong': '0,0',
        })
        self.assertDictEqual(response.context['images'], {})
