from django.db import models
from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    is_sub = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if isinstance(self.parent, self.__class__):
            self.is_sub = True
        else:
            self.is_sub = False

    def __str__(self):
        return f'{self.name}'
