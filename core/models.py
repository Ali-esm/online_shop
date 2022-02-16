from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import BaseManager


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
