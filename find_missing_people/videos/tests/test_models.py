from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from videos.models import Video, ImagesFromVideo
from listings.models import MissingPerson


class TestVideoModel(TestCase):
    def setUp(self):
        self.data = Video.objects.create(id=0, title='test')

    def test_video_name(self):
        self.assertEqual(str(self.data), 'test')


class TestImagesFromVideoModel(TestCase):
    def setUp(self):
        self.time = timezone.now()
        self.user = User.objects.create(id=0, username='test', password='test', email='test@test.com')
        self.missing_person = MissingPerson.objects.create(id=0, name='test', state='CA', sex='M', age=20, lat=20, list_date=self.time,
                                                           missing_date=self.time, photo_main='test', lng=20, is_accepted=True,
                                                           user=self.user)
        self.data = ImagesFromVideo.objects.create(name='test', photo='test', date=self.time, user=self.user,
                                                   missing_person=self.missing_person)
    
    def test_images_from_video_name(self):
        self.assertEqual(str(self.data), 'test')
