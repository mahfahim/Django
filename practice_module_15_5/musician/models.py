from django.db import models

class Musician(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    phone = models.CharField(max_length=20)
    instrument = models.CharField( max_length=50)
    
