import datetime
from django.test import TestCase
from ..models import OffCode


class OffCodeTest(TestCase):

    def setUp(self) -> None:
        tomorrow = datetime.timedelta(days=1) + datetime.datetime.now()
        yesterday = datetime.timedelta(days=-1) + datetime.datetime.now()

        self.off1 = OffCode.objects.create(amount=20, type='PE', expire_time=tomorrow,
                                           code='test', max_value=5000)
        self.off2 = OffCode.objects.create(amount=10, type='PE', expire_time=yesterday,
                                           code='test')
        self.off3 = OffCode.objects.create(amount=10000, type='PR', expire_time=tomorrow,
                                           code='test')
        self.off4 = OffCode.objects.create(amount=50000, type='PR', expire_time=tomorrow,
                                           code='test', used=True)

    def test_by_percent(self):
        self.assertEqual(self.off1.profit_amount(10_000), 2000)
        self.assertEqual(self.off1.profit_amount(8000), 1600)

    def test_by_price(self):
        self.assertEqual(self.off3.profit_amount(20000), 10000)
        self.assertEqual(self.off3.profit_amount(99000), 10000)

    def test_max_value(self):
        self.assertEqual(self.off1.profit_amount(30_000), 5000)
        self.assertEqual(self.off1.profit_amount(100_000), 5000)
        self.assertEqual(self.off1.profit_amount(251_111), 5000)

    def test_off_code_is_used(self):
        self.assertEqual(self.off4.profit_amount(1000000), None)
        self.assertEqual(self.off4.profit_amount(50000), None)

    def test_off_code_expired(self):
        self.assertEqual(self.off2.profit_amount(2000000), None)
        self.assertEqual(self.off2.profit_amount(1000), None)
        self.assertEqual(self.off2.profit_amount(10), None)
