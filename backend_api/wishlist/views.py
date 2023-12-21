from rest_framework import generics
from .models import WishlistItem
from .serializers import WishlistItemSerializer

class WishlistItemListCreateView(generics.ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

class WishlistItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
