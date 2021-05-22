from django.db import models
from datetime import datetime

class Contact(models.Model):
    missing_person_name = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    from_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    last_seen = models.DateTimeField(default=datetime.now, blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.from_name