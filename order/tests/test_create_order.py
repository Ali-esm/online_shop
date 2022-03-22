from django.test import TestCase
from ..models import Order
from customer.models import Customer, User


class OrderTest(TestCase):

    def setUp(self) -> None:
        self.test_user = User.objects.create_user(username='09123456789', password='1234', phone_number='09123456789')
        self.test_customer = Customer.objects.create(user=self.test_user)
        self.test_order = Order.objects.create_order(customer_id=self.test_customer.id, total_price=100, status='P')
        self.test_order2 = Order.objects.create_order(customer_id=self.test_customer.id, total_price=100, status='C')
        self.test_order2 = Order.objects.create_order(customer_id=self.test_customer.id, total_price=100, status='C')
        self.test_order3 = Order.objects.create_order(customer_id=self.test_customer.id, total_price=100, status='U')
        self.test_order4 = Order.objects.create_order(customer_id=self.test_customer.id, total_price=100, status='U')

    def test_unpaid_order_count(self):
        self.assertEqual(Order.objects.filter(status='U').count(), 1)

    def test_all_orders_count(self):
        self.assertEqual(Order.objects.all().count(), 4)