from django.contrib.auth import views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .forms import LoginForm, SignUpForm


class CustomerLoginView(views.LoginView):
    """
    Customization LoginView for Login Customers
    """
    template_name = 'customer/login.html'
    authentication_form = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home_view'))
        return super().get(request, *args, **kwargs)


