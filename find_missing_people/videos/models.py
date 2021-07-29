from django.conf import settings
from django.db import models

from listings.models import MissingPerson


class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.title


class ImagesFromVideo(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='taken_photos/%Y/%m/%d/', blank=True)
    date = models.DateField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    missing_person = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
