from django.db import models

# Create your models here.


class MissingPeople(models.Model):
    name = models.CharField(max_length=45)
    image_url = models.CharField(db_column='imageUrl', max_length=250)  # Field name made lowercase.
    email = models.CharField(max_length=100)
    found_time = models.DateTimeField(db_column='foundTime', blank=True, null=True)  # Field name made lowercase.

    def save_request(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'missing_people'