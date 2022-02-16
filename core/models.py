from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from .manager import BaseManager
from .validators import phone_validator


class MyUserManager(UserManager):
    """
    Customization Django UserManager for change username to phone_number field
    """

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields["phone_number"]
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    """
    Customization Django User to add phone_number field & change username field to phone_number field
    """
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    phone_number = models.CharField(max_length=11, unique=True, verbose_name=_('Phone Number'),
                                    validators=[phone_validator], help_text=_('Enter Your Phone Number'))

    USERNAME_FIELD = 'phone_number'
    objects = MyUserManager()


class BaseModel(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('create time'))
    update_timestamp = models.DateTimeField(auto_now=True, verbose_name=_('last update'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))
    is_deleted = models.BooleanField(default=False, verbose_name=_('delete'))

    def activate(self):
        self.is_active = True
        self.save()

    def inactivate(self):
        self.is_active = False
        self.save()

    def get_delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

    objects = BaseManager()

    class Meta:
        abstract = True
