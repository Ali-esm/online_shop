from django.contrib.auth import views, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from core.models import User
from .models import Customer
from .forms import LoginForm, SignUpForm


class CustomerSignUpView(views.FormView):
    template_name = 'customer/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        user = User.objects.create_user(password=form.cleaned_data['password2'],
                                        phone_number=form.cleaned_data['phone_number'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        customer = Customer.objects.create(user=user)
        login(self.request, user)
        return redirect(reverse('home_view'))


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


