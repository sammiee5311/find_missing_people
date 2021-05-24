from django.db import models
from datetime import datetime
from django.conf import settings

class Listing(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    lat = models.DecimalField(max_digits=15, decimal_places=6,blank=True)
    lng = models.DecimalField(max_digits=15, decimal_places=6,blank=True)
    is_private = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)
    missing_date = models.DateTimeField(default=datetime.now, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_accepted = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MissingPeople(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    lat = models.DecimalField(max_digits=15, decimal_places=6,blank=True)
    lng = models.DecimalField(max_digits=15, decimal_places=6,blank=True)
    is_private = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)
    missing_date = models.DateTimeField(default=datetime.now, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_accepted = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

