from django.urls import path
from .views import CartItemListCreateView, RemoveFromCart, AddToCartView

urlpatterns = [
    path('cart-items/', CartItemListCreateView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', RemoveFromCart.as_view(), name='cart-item-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
]
