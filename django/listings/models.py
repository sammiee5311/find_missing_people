from django.db import models
from datetime import datetime
from requestors.models import Requestor

class Listing(models.Model):
    requestor = models.ForeignKey(Requestor, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_private = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)
    missing_date = models.DateTimeField(default=datetime.now, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name

