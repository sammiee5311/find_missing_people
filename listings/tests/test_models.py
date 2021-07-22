from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from listings.models import MissingPerson


class TestMissingPersonModel(TestCase):
    def setUp(self):
        self.time = timezone.now()
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.comm')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user)

    def test_missing_person_name(self):
        self.assertEqual(str(self.missing_person), 'test')
