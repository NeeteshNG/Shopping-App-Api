from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework import status

class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('productId')
        
        if user and product_id:
            try:
                # Check if the product already exists in the user's cart
                cart_item = CartItem.objects.filter(user=user, product_id=product_id).first()
                
                if cart_item:
                    # If the item exists, increment the quantity
                    cart_item.quantity += 1
                    cart_item.save()
                    serializer = CartItemSerializer(cart_item)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    # If the item does not exist, create a new cart item with quantity=1
                    cart_item = CartItem.objects.create(user=user, product_id=product_id, quantity=1)
                    serializer = CartItemSerializer(cart_item)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
