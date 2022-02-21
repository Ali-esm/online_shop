from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, BaseDiscount


class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('product name'))
    brand = models.CharField(max_length=100, verbose_name=_('brand name'))
    price = models.PositiveIntegerField(verbose_name=_('price'), help_text=_('set product price'))
    is_exist = models.BooleanField(default=True, verbose_name=_('available'))
    image = models.FileField(verbose_name=_('image'), upload_to='media/%Y-%m-%d',
                             default='not_available.jpg')
    detail = models.JSONField(blank=True, null=True, verbose_name=_('product detail'),
                              help_text=_('detail for product'))
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, related_name='products',
                                 blank=True, null=True, default=None, verbose_name=_('discount'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def update_existence(self):
        """
        this method used for update existence of product
        """
        if self.is_exist:
            self.is_exist = False
            self.save()
        else:
            self.is_exist = True
            self.save()


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    is_sub = models.BooleanField(default=False, verbose_name=_('is sub'))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name=_('parent'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Customization save method for check if category obj is_sub category set is_sub field to True
        """
        if self.is_sub is False and isinstance(self.parent, self.__class__):
            self.is_sub = True
        else:
            self.is_sub = False
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name}'


class Discount(BaseDiscount):
    name = models.CharField(default='discount', max_length=100, verbose_name=_('name'))

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')

    def __str__(self):
        return f"{self.name}"


class OffCode(BaseDiscount):
    max_value = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('maximum value'),
                                            help_text=_('maximum value of discount'))
    code = models.CharField(max_length=10, verbose_name=_('discount code'),
                            help_text=_('set code for discount'))
    used = models.BooleanField(default=False, verbose_name=_('is used'),
                               help_text=_('set off code used or not'))

    class Meta:
        verbose_name = _('Off Code')
        verbose_name_plural = _('Off Codes')

    def profit_amount(self, price: int):
        """
        Customization profit_amount for check if off code not used & not expired calculate profit
        """
        if self.used or self.is_expire():
            return None
        elif self.type == 'PR':
            return min(self.amount, price)
        raw_profit = int((self.amount / 100) * price)
        return min(raw_profit, self.max_value) if self.max_value else raw_profit
