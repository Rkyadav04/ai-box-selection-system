from django.contrib import admin

from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name', 
        'recommended_box', 
        'created_at', 
        
    )
    search_fields = ('customer_name',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order', 
        'product', 
        'quantity', 
    )
    