from django.db import models
import uuid

class MyModel(models.Model):
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    null_boolean_field = models.BooleanField(null=True)  # Fixed deprecated field
    slug_field = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"MyModel {self.pk}"
