from rest_framework import serializers

from .models import ShippingBox


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