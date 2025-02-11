from django.db import models
from musician_app.models import Musician

# Create your models here.
RATING_CHOICES = [
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
]
   
class Album(models.Model):
    album_name = models.CharField( max_length=50)
    release_date = models.DateField( auto_now=False, auto_now_add=False)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5,
        help_text="Select a rating between 1 and 5"
    )
    album_number = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    
    