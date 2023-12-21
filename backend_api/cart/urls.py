from django.urls import path
from .views import CartItemListCreateView, CartItemDetailView

urlpatterns = [
    path('cart-items/', CartItemListCreateView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
]
