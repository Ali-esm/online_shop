from django.contrib import admin
from .models import Customer, Address


class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    max_num = 1


class CustomerAdmin(admin.ModelAdmin):
    fields = ['user', 'gender', 'birth_date']
    list_display = ['get_phone', 'get_full_name']
    inlines = (AddressInline,)

    # get_phone.short_description = "Phone"  # this line is shown instead of get phone on title


class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'province', 'zip_code', 'get_customer_phone']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)