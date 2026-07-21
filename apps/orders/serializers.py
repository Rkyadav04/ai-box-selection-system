from rest_framework import serializers

from apps.boxes.models import ShippingBox
from apps.products.models import Product

from apps.products.serializers import ProductSerializer
from apps.boxes.serializers import ShippingBoxSerializer

from .models import Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "length",
            "width",
            "height",
            "weight",
        )


class ShippingBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingBox
        fields = (
            "id",
            "name",
            "length",
            "width",
            "height",
            "max_weight",
            "cost",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "quantity",
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "customer_name",
        )
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product",
            "quantity",
        )

class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    recommended_box = ShippingBoxSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "customer_name",
            "recommended_box",
            "items",
            "created_at",
        )