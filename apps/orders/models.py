from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from apps.boxes.models import ShippingBox
from apps.common.models import TimeStampedModel
from apps.products.models import Product
class Order(TimeStampedModel):
    customer_name = models.CharField(max_length=255, blank=True, default="",)

    recommended_box = models.ForeignKey(
        'boxes.ShippingBox',
         on_delete=models.SET_NULL,
         null=True, 
         blank=True,
         related_name='recommended_orders',
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.pk}"
        
        
        
    def get_total_weight(self) -> Decimal:
            total = Decimal("0.00")
            for item in self.items.select_related('product'):
                total += item.product.weight * item.quantity
            return total
        
    def get_packing_dimensions(self):
            length = Decimal("0.00")
            width = Decimal("0.00")
            height = Decimal("0.00")

            for item in self.items.select_related('product'):
                product = item.product
                length = max(length, product.length)
                width = max(width, product.width)
                height += product.height * item.quantity

            return {
                "length": length,
                "width": width,
                "height": height,
            }
        
class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name='items'
        )
    
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='order_items'
        )
    
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1,)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"    