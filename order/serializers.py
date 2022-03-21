from rest_framework import serializers

from order.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    off_code = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'off_code', 'total_price', 'status']


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity']

