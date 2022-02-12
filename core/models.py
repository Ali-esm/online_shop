from django.db import models
from .manager import BaseManager


class BaseModel(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

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
