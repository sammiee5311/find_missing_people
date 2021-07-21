from django.db import models
from listings.models import MissingPerson

from django.conf import settings


class ImagesFromVideo(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='taken_photos/%Y/%m/%d/', blank=True)
    date = models.DateField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    missing_person = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
