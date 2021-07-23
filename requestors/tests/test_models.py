from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from requestors.models import Requestor


class TestRequestorModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.com')
        self.requestor = Requestor.objects.create(name='test', phone='123456', email='test@test.com', 
                                                  registered_date=timezone.now(), user=self.user)

    def test_requestor_name(self):
        self.assertEqual(str(self.requestor), 'test')
