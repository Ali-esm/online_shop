import datetime
from django.test import TestCase
from ..models import Discount


class DiscountTest(TestCase):

    def setUp(self) -> None:
        tomorrow = datetime.timedelta(days=1) + datetime.datetime.now()
        yesterday = datetime.timedelta(days=-1) + datetime.datetime.now()

        self.discount1 = Discount.objects.create(name='discount1', type='PR', amount=5000,
                                                 expire_time=tomorrow)
        self.discount2 = Discount.objects.create(name='discount2', type='PR', amount=10000,
                                                 expire_time=yesterday)
        self.discount3 = Discount.objects.create(name='discount3', type='PE', amount=10,
                                                 expire_time=tomorrow)
        self.discount4 = Discount.objects.create(name='discount4', type='PE', amount=20,
                                                 expire_time=yesterday)

    def test_discount_not_expired(self):
        self.assertFalse(self.discount1.is_expire())
        self.assertTrue(self.discount2.is_expire())

    def test_discount_expired(self):
        self.assertTrue(self.discount2.is_expire())
        self.assertFalse(self.discount1.is_expire())

    def test_get_type(self):
        self.assertEqual(self.discount1.get_type, 'price')
        self.assertEqual(self.discount2.get_type, 'price')

    def test_profit_amount_expire_discount(self):
        self.assertEqual(self.discount2.profit_amount(20000), None)
        self.assertEqual(self.discount4.profit_amount(300000), None)

    def test_profit_amount_gt_discount(self):
        self.assertEqual(self.discount1.profit_amount(20000), 5000)
        self.assertEqual(self.discount1.profit_amount(30000000), 5000)
        self.assertEqual(self.discount1.profit_amount(30000000), 5000)

    def test_profit_amount_lt_discount(self):
        self.assertEqual(self.discount1.profit_amount(2000), 2000)
        self.assertEqual(self.discount1.profit_amount(200), 200)
        self.assertEqual(self.discount1.profit_amount(3), 3)

    def test_discount_str(self):
        self.assertEqual(str(self.discount1), 'discount1')
        self.assertEqual(str(self.discount2), 'discount2')

    def test_discount_profit_amount_by_percent(self):
        self.assertEqual(self.discount3.profit_amount(30000), 3000)
        self.assertEqual(self.discount3.profit_amount(100_000), 10_000)