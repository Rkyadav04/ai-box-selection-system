from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'length', 
        'width', 
        'height', 
        'weight', 
        'created_at', 
        'updated_at')
    search_fields = ('name',)
    