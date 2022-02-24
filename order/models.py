from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel

from customer.models import Customer
from product.models import Product, OffCode


class Order(BaseModel):

    class Status(models.TextChoices):
        PAID = 'P', _('paid')
        UNPAID = 'U', _('unpaid')
        CANCELED = 'C', _('canceled')

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.RESTRICT,
                                 verbose_name=_('customer'))
    off_code = models.ForeignKey(OffCode, related_name='orders', on_delete=models.SET_NULL,
                                 null=True, blank=True, verbose_name=_('off code'))
    total_price = models.IntegerField(verbose_name=_('total price'))
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.UNPAID,
                              verbose_name=_('status'))

    @property
    def get_total_price(self):
        """
        for calculating all order items price
        """
        return sum(item.get_price() for item in self.orderitem_set.all())

    def __str__(self):
        return f'< order #{self.id} {self.status} {self.total_price} >'


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('order'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order items')

    @property
    def get_price(self):
        """
         for calculating product final price minus discount
        """
        profit_amount = self.product.discount.profit_amount(self.product.price)
        return (self.product.price - profit_amount) * self.quantity

    def __str__(self):
        return f'< {self.product.name}: {self.quantity} >'
