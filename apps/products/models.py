from django.db import models

# Create your models here.
from apps.common.models import TimestampedModel

class Product(TimestampedModel):
    name = models.CharField(max_length=255)
    length = models.DecimalField(max_digits=8, decimal_places=2)
    width = models.DecimalField(max_digits=8, decimal_places=2)
    height = models.DecimalField(max_digits=8, decimal_places=2)

    weight = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
