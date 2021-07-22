from datetime import datetime

from django.conf import settings
from django.db import models

from listings.models import MissingPerson


class Contact(models.Model):
    missing_person_name = models.CharField(max_length=200)
    listing = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)
    from_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    last_seen = models.DateTimeField(default=datetime.now, blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.from_name
