from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .models import Product, Category, Discount, OffCode


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'is_exist', 'category']
    list_editable = ['price', ]
    list_filter = ['price', 'is_exist']
    search_fields = ['name', 'brand']
    actions = ['set_not_exist', 'set_is_exist']

    @admin.action(description='Set selected Product Not available')
    def set_not_exist(self, request, queryset):
        updated = queryset.update(is_exist=False)
        self.message_user(request, ngettext(
            f'{updated} product was successfully marked as not available.',
            f'{updated} products were successfully marked as not available.',
            updated,
        ), messages.SUCCESS)

    @admin.action(description='Set selected Product is available')
    def set_is_exist(self, request, queryset):
        updated = queryset.update(is_exist=True)
        self.message_user(request, ngettext(
            f'{updated} product was successfully marked as available.',
            f'{updated} products were successfully marked as available.',
            updated,
        ), messages.SUCCESS)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(OffCode)
