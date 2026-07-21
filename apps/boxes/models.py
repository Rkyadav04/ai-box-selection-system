from django.db import models

from apps.common.models import TimestampedModel

class ShippingBox(TimestampedModel):
    name = models.CharField(max_length=255)
    length = models.DecimalField(max_digits=8, decimal_places=2)
    width = models.DecimalField(max_digits=8, decimal_places=2)
    height = models.DecimalField(max_digits=8, decimal_places=2)

    max_weight = models.DecimalField(max_digits=8, decimal_places=2)

    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["cost"]
    
    def __str__(self):
        return self.name