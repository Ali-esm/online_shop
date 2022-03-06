from django.contrib.auth import views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import LoginForm, SignUpForm
from django.views import View, generic

from core.models import User
from .models import Customer, Address


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
        return redirect(reverse('customer:profile_view'))


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


class CustomerLogoutView(views.LogoutView):
    """
    Customization LogoutView for Logout Customers
    """
    pass


class CustomerProfileView(LoginRequiredMixin, View):

    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        customer = user.customer
        main_address = customer.address_set.first()
        context = {
            'customer': customer,
            'address': main_address,
        }
        return render(request, 'customer/profile.html', context=context)


class CustomerAddressView(LoginRequiredMixin, View):

    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        customer = user.customer
        addresses = customer.address_set.all()
        context = {
            'addresses': addresses,
        }
        return render(request, 'customer/profile_address_list.html', context=context)


class CustomerAddressDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Address
    success_url = reverse_lazy('customer:address_view')



