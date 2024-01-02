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

class AddToWishlistView(generics.CreateAPIView):
    serializer_class = WishlistItemSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('productId')
        
        if user and product_id:
            try:
                wishlist_Item = WishlistItem.objects.filter(user=user, product_id=product_id).first()
                
                if wishlist_Item:
                    wishlist_Item.save()
                    serializer = WishlistItemSerializer(wishlist_Item)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    wishlist_Item = WishlistItem.objects.create(user=user, product_id=product_id)
                    serializer = WishlistItemSerializer(wishlist_Item)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class WishlistItemDeleteView(generics.DestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

    def destroy(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('productId')
        
        if user and product_id:
            try:
                wishlist_item = WishlistItem.objects.get(user=user, product_id=product_id)
                wishlist_item.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except WishlistItem.DoesNotExist:
                return Response({'error': 'Item does not exist'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)