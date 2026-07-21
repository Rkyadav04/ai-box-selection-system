from django.urls import path

from .views import (
    OrderDetailView,
    OrderListCreateView,
    RecommendBoxView,
    OrderItemListCreateView,
    OrderItemDetailView,
)

urlpatterns = [
    path(
        "",
        OrderListCreateView.as_view(),
        name="order-list-create",
    ),

    path(
        "<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail",
    ),

    path(
        "<int:pk>/recommend/",
        RecommendBoxView.as_view(),
        name="recommend-box",
    ),
    path(
        "items/",
        OrderItemListCreateView.as_view(),
        name="order-item-list-create",
    ),

    path(
        "items/<int:pk>/",
        OrderItemDetailView.as_view(),
        name="order-item-detail",
    ),

]