from django.contrib import admin

from .models import ShippingBox

@admin.register(ShippingBox)
class ShippingBoxAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'max_weight',
        'cost',
    ) 
        
    search_fields = ('name',)