from decimal import Decimal

from django.test import TestCase

from apps.boxes.models import ShippingBox
from apps.orders.models import Order, OrderItem
from apps.products.models import Product
from apps.recommendations.exceptions import NoSuitableBoxFound
from apps.recommendations.services import BoxRecommendationService


class BoxRecommendationServiceTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2,
        )

        self.small = ShippingBox.objects.create(
            name="Small",
            length=20,
            width=20,
            height=10,
            max_weight=5,
            cost=50,
        )

        self.medium = ShippingBox.objects.create(
            name="Medium",
            length=40,
            width=30,
            height=20,
            max_weight=10,
            cost=120,
        )

        self.large = ShippingBox.objects.create(
            name="Large",
            length=60,
            width=40,
            height=40,
            max_weight=20,
            cost=200,
        )

        self.order = Order.objects.create(
            customer_name="John"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )

        self.service = BoxRecommendationService()

#Test cases for BoxRecommendationService

#Test Case 1:

    def test_calculate_requirements(self):
      requirements = self.service.calculate_requirements(self.order)

      self.assertEqual(requirements["length"], Decimal("30"))
      self.assertEqual(requirements["width"], Decimal("20"))
      self.assertEqual(requirements["height"], Decimal("10"))
      self.assertEqual(requirements["weight"], Decimal("4"))

#Test Case 2:
    def test_find_compatible_boxes(self):
      requirements = self.service.calculate_requirements(self.order)
      boxes = self.service.find_compatible_boxes(requirements)
      self.assertEqual(len(boxes), 2)

#Test Case 3:
    def test_select_cheapest_box(self):
      box = self.service.recommend(self.order)
      self.assertEqual(box.name, "Medium")

#Test Case 4:
    def test_no_suitable_box_found(self):

        ShippingBox.objects.all().delete()
        with self.assertRaises(NoSuitableBoxFound):
            self.service.recommend(self.order)
