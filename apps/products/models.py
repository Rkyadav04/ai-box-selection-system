from django.db import models
from django.core.validators import MinValueValidator

from apps.common.models import TimeStampedModel, DimensionMixin

class Product(TimeStampedModel, DimensionMixin):
    name = models.CharField(max_length=255)

    weight = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
