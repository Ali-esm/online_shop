from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from core.models import User
from core.forms import CustomUserCreationForm
from .models import Address


class SignUpForm(CustomUserCreationForm):
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'col-10 p-2',
                                    'placeholder': _('Password'),
                                }))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'col-10 p-2',
                                    'placeholder': _('Confirm Password')
                                }))

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'phone_number': '',
            'first_name': '',
            'last_name': '',
        }

        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('Phone'),
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('First Name'),
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('Last Name'),
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-10 p-2',
        'placeholder': _('Phone number'),
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'col-10 p-2',
        'placeholder': _('Password'),
    }))

    class Meta:
        model = User
        fields = ['username', 'password']

        error_messages = {
            'login_error': _("Phone Number or Password is Incorrect")
        }

        labels = {
            'username': '',
            'password': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('Phone'),
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('Password')
            })
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'province', 'street', 'alley', 'No', 'zip_code']
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'province': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'street': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'alley': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'No': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'zip_code': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }
    
    
    
    