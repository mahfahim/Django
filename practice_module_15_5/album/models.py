   
from django.db import models
from musician.models import Musician

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    def __str__(self):
        return self.album_name
