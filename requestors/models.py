from datetime import datetime

from django.db import models

from django.conf import settings


class Requestor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    registered_date = models.DateField(default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
