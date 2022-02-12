from django.db import models


class BaseManager(models.Manager):

    def get_queryset(self):
        """
        change default manager queryset to get objects is not logical deleted.
        """
        return super().get_queryset().filter(is_deleted=False)

    def get_all(self):
        """
        this method used to get all model queryset
        """
        return super().get_queryset()

    def get_active_list(self):
        """
        this method used to get all active model queryset
        """
        return super().get_queryset().filter(is_active=True, is_deleted=False)

    def get_inactive_list(self):
        """
        this method used to get all inactivated model queryset
        """
        return super().get_queryset().filter(is_active=False)

    def get_deleted_list(self):
        """
        this method used to get all deleted model queryset
        """
        return super().get_queryset().filter(is_deleted=True)



