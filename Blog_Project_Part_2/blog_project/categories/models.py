from django.db import models

# Create your models here.
class Category(models.Model): ###
    name = models.CharField(max_length=100) ###
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True) ###
    
    def __str__(self): 
        return self.name ###
    
# A slug is a URL-friendly version of name, used in SEO-friendly URLs.
# Example: "Technology" → "technology"

# max_length=100 → Maximum length of 100 characters.
# unique=True → Ensures each slug is unique (no duplicates).
# null=True → Allows storing NULL (empty values).
# blank=True → Allows leaving this field empty in Django forms.