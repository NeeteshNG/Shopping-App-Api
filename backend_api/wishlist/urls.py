from django.urls import path
from .views import WishlistItemListCreateView, WishlistItemDetailView, WishlistItemDeleteView

urlpatterns = [
    path('wishlist-items/', WishlistItemListCreateView.as_view(), name='wishlist-item-list'),
    path('wishlist-items/<int:pk>/', WishlistItemDetailView.as_view(), name='wishlist-item-detail'),
    path('wishlist-items/delete/<int:pk>/', WishlistItemDeleteView.as_view(), name='wishlist-item-delete'),
]
