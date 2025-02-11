from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assign_date = models.DateTimeField()
    category = models.ManyToManyField(Category)
    is_complete = models.BooleanField(default=False)
def __str__(self):
    return self.title 

