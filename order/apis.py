from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order, OrderItem
from product.models import Product, OffCode
from product.serializers import ProductSerializer, OffCodeSerializer
from order.serializers import OrderSerializer, OrderItemSerializer
from customer.models import Customer


class GetProductCookieAPIView(APIView):

    def get(self, request):
        product_list = []
        cookie_dict = request.session.items()
        for key, value in cookie_dict:
            if key.startswith('p'):
                product_id = key[1:]
                product = Product.objects.get(id=product_id)
                product_list.append(product)
        products = ProductSerializer(product_list, many=True)
        return Response(products.data, status=200)


class OrderItemCountPartialUpdate(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def patch(self, request):
        order_item = OrderItem.objects.get(id=request.GET['item'])
        item_serializer = OrderItemSerializer(order_item, request.data, partial=True)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(data=item_serializer.data, status=201)
        return Response(data=item_serializer.errors, status=400)


class OrderOffCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def patch(self, request):
        customer = Customer.objects.get(user__phone_number=request.user.phone_number)
        order = customer.orders.get(status__exact='U')
        if not order.off_code_used():
            serializer = OffCodeSerializer(data=request.data)
            if serializer.is_valid():
                off_code = OffCode.objects.get(code__exact=serializer.validated_data['code'])
                if not off_code.is_expire():
                    order.off_code = off_code
                    order.save()
                    return Response(data={'ok': 1}, status=201)
                return Response(data={'fail': 0}, status=400)
        return Response(data={'fail': 0}, status=400)