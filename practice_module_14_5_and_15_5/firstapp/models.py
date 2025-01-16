from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, default='2025-01-01T00:00:00')
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='img/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    related_field = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
