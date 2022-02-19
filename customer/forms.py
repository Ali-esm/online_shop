from django import forms
from django.utils.translation import gettext_lazy as _
from core.models import User
from core.forms import CustomUserCreationForm


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
        help_texts = {

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


class LoginForm(forms.ModelForm):

    class Meta:
        model= User
        fields = ['phone_number', 'password']

        labels = {
            'phone_number': '',
            'password': '',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('Phone'),
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'col-10 p-2',
                'placeholder': _('Password')
            })
        }