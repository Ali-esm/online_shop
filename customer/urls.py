from django.urls import path
from django.views.generic import TemplateView
from.views import CustomerLoginView, CustomerSignUpView, CustomerLogoutView,\
    CustomerProfileView

app_name = 'customer'
urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login_view'),
    path('signup/', CustomerSignUpView.as_view(), name='signup_view'),
    path('logout/', CustomerLogoutView.as_view(), name='logout_view'),
    path('profile/', CustomerProfileView.as_view(), name='profile_view'),
]