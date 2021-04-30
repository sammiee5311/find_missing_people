from django.db import models
from datetime import datetime

class Requestor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    registered_date = models.DateField(default=datetime.now)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name

