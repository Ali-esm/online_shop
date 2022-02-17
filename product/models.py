from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel, BaseDiscount


class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    is_sub = models.BooleanField(default=False, verbose_name=_('is sub'))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name=_('parent'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
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
