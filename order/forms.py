from django import forms
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ['is_deleted', 'address', 'is_active']
        widgets = {
            'status': forms.HiddenInput(),
            'customer': forms.HiddenInput(),
            'total_price': forms.HiddenInput(),
            'final_price': forms.HiddenInput(),
            'off_code': forms.HiddenInput(),
        }


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        exclude = ['is_deleted', 'is_active']
        widgets = {
            'product': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }