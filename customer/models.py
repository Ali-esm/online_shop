from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import User, BaseModel


class Customer(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('male')
        FEMALE = 'F', _('female')
        NONE = 'N', _('none')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.NONE,
                              verbose_name=_('gender'))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_('birth date'))

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def get_full_name(self):
        return self.user.get_full_name()

    def get_phone(self):
        return self.user.phone_number

    def __str__(self):
        return f'{self.user.username}'


class Address(BaseModel):
    city = models.CharField(max_length=30, verbose_name=_('city'))
    province = models.CharField(max_length=30, verbose_name=_('province'))
    street = models.CharField(max_length=30, verbose_name=_('street'))
    alley = models.CharField(max_length=30, verbose_name=_('alley'))
    No = models.PositiveSmallIntegerField(blank=True, null=True, default=None, verbose_name=_('NO'))
    zip_code = models.CharField(max_length=10, verbose_name=_('zip code'))
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def get_customer_phone(self):
        return self.customer.get_phone()

    def __str__(self):
        return f'{self.city}'
