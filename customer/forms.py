from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from core.models import User
from core.forms import CustomUserCreationForm
from .models import Address, Customer


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

    def clean_zip_code(self):
        """
        This method used for check zip code length equals to 10
        """
        zip_code = self.cleaned_data['zip_code']
        if len(zip_code) != 10:
            raise ValidationError(_("Zip code length must be 10"))
        return zip_code


class UpdateUserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
        ('N', 'None'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, initial=GENDER_CHOICES[2][0])
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    phone = forms.CharField(disabled=True, label='Phone Number')

    class Meta:
        model = User
        fields = ['phone', 'last_name', 'first_name', 'birth_date', 'gender']


