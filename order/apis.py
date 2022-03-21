from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order, OrderItem
from product.models import Product
from product.serializers import ProductSerializer
from order.serializers import OrderSerializer, OrderItemSerializer


class GetProductCookieAPIView(APIView):

    def get(self, request):
        product_list = []
        for key, value in request.COOKIES.items():
            if key.startswith('p'):
                product_id = key[1:]
                product = Product.objects.get(id=product_id)
                product_list.append(product)
        products = ProductSerializer(product_list, many=True)
        return Response(products.data, status=200)