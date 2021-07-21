from django.test import TestCase
from requestors.models import Requestor


class TestRequestorModel(TestCase):
    def setUp(self):
        self.data = Requestor.objects.create(name='test', phone='123456', email='test@test.com', user_id=0)

    def test_requestor_name(self):
        self.assertEqual(str(self.data), 'test')
