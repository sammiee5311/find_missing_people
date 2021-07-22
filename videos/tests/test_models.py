from django.test import TestCase

from videos.models import Video


class TestVideoModel(TestCase):
    def setUp(self):
        self.data = Video.objects.create(id=0, title='test')

    def test_video_name(self):
        self.assertEqual(str(self.data), 'test')
