from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from contacts.models import Contact
from listings.models import MissingPerson


class TestContactModels(TestCase):
    def setUp(self):
        self.time = timezone.now()
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.com')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user)
        self.contact = Contact.objects.create(from_name='test', missing_person=self.missing_person, email='test@test.com', phone=123456789,
                                              message='test', last_seen=self.time, contact_date=self.time, user=self.user)
    
    def test_contact_from_name(self):
        self.assertEqual(str(self.contact), 'test')
