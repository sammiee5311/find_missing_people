from django.db import models

class ImagesFromVideo(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='taken_photos/%Y/%m/%d/', blank=True)
    date = models.DateField(blank=True)
    user_id = models.IntegerField()
    missing_person_id = models.IntegerField()

    def __str__(self):
        return self.name