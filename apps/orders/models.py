from django.db import models

from apps.common.models import TimestampedModel
from apps.products.models import Product
class Order(TimestampedModel):
    customer_name = models.CharField(max_length=255)

    recommended_box = models.ForeignKey(
        'boxes.ShippingBox',
         on_delete=models.SET_NULL,
         null=True, 
         blank=True,
         related_name='recommended_orders',
    )

def __str__(self):
    return f"Order #{self.pk}"

class OrderItem(TimestampedModel):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='items'
        )
    
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"    