from django.test import TestCase

from apps.orders.models import Order, OrderItem
from apps.products.models import Product

from rest_framework.test import APITestCase
from rest_framework import status
class OrderModelTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name="Mouse",
            length=10,
            width=5,
            height=3,
            weight=1,
        )

        self.order = Order.objects.create(
            customer_name="Ravinder"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )



#Test for OrderItem creation:

#Test case 1:
    def test_total_weight(self):
        self.assertEqual(
            self.order.get_total_weight(),
            2,
     )
        
#Test case 2:
    def test_packing_dimensions(self):

        dimensions = self.order.get_packing_dimensions()

        self.assertEqual(dimensions["length"], 10)
        self.assertEqual(dimensions["width"], 5)
        self.assertEqual(dimensions["height"], 6)

#Test case 3:
    def test_string_representation(self):
        self.assertEqual(
            str(self.order),
            f"Order #{self.order.pk}"
    )
        
class OrderAPITest(APITestCase):

    def test_create_order(self):

        response = self.client.post(
            "/api/orders/",
            {
                "customer_name": "Ravinder"
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        
#TEest Case 4: Test List Orders API endpoint

    def test_list_orders(self):

        Order.objects.create(
            customer_name="Test"
    )

        response = self.client.get("/api/orders/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
    )
        
#Test Case 5: List Retrieve Order API endpoint

    def test_retrieve_order(self):

        order = Order.objects.create(
            customer_name="Test"
        )

        response = self.client.get(
            f"/api/orders/{order.id}/"
    )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
    )
