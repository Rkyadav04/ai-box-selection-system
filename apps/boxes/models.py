from django.db import models
from django.core.validators import MinValueValidator
from apps.common.models import TimeStampedModel, DimensionMixin

class ShippingBox(TimeStampedModel, DimensionMixin):
    name = models.CharField(max_length=255)

    max_weight = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])

    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])

    class Meta:
        ordering = ["cost"]
        verbose_name = "Shipping Box"
        verbose_name_plural = "Shipping Boxes"
    
    def __str__(self):
        return self.name