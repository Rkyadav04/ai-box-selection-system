from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.models import Order, OrderItem
from apps.recommendations.exceptions import NoSuitableBoxFound
from apps.recommendations.services import BoxRecommendationService

from .serializers import (
    OrderCreateSerializer,
    OrderDetailSerializer,
    OrderItemCreateSerializer,
)


class OrderListCreateView(generics.ListCreateAPIView):
    """
    GET  -> List all orders
    POST -> Create new order
    """

    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer

        return OrderDetailSerializer


class OrderDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single order.
    """

    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

class OrderItemListCreateView(generics.ListCreateAPIView):
    """
    GET -> List all order items
    POST -> Create a new order item
    """

    queryset = OrderItem.objects.select_related(
        "order",
        "product",
    )

    serializer_class = OrderItemCreateSerializer

class OrderItemDetailView(generics.RetrieveAPIView):
    """
    Retrieve one order item.
    """

    queryset = OrderItem.objects.select_related(
        "order",
        "product",
    )

    serializer_class = OrderItemCreateSerializer

class RecommendBoxView(APIView):
    """
    Recommend the cheapest compatible shipping box.
    """

    def post(self, request, pk):

        order = get_object_or_404(Order, pk=pk)

        service = BoxRecommendationService()

        try:

            box = service.recommend(order)

            order.recommended_box = box
            order.save(update_fields=["recommended_box"])

            serializer = OrderDetailSerializer(order)

            return Response(
                {
                    "message": "Shipping box recommended successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except NoSuitableBoxFound as exc:

            return Response(
                {
                    "message": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )