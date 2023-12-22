from rest_framework import generics
from .models import WishlistItem
from .serializers import WishlistItemSerializer
from rest_framework.response import Response
from rest_framework import status

class WishlistItemListCreateView(generics.ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

class WishlistItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

class AddToCartView(generics.CreateAPIView):
    serializer_class = WishlistItemSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('productId')
        
        if user and product_id:
            try:
                # Check if the product already exists in the user's cart
                cart_item = WishlistItem.objects.filter(user=user, product_id=product_id).first()
                
                if cart_item:
                    cart_item.save()
                    serializer = WishlistItemSerializer(cart_item)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    cart_item = WishlistItem.objects.create(user=user, product_id=product_id)
                    serializer = WishlistItemSerializer(cart_item)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
