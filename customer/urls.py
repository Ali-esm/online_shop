from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'customer'
urlpatterns = [
    path('login/', views.CustomerLoginView.as_view(), name='login_view'),
    path('signup/', views.CustomerSignUpView.as_view(), name='signup_view'),
    path('logout/', views.CustomerLogoutView.as_view(), name='logout_view'),
    path('profile/', views.UserProfileUpdateView.as_view(), name='profile_view'),
    path('address/', views.CustomerAddressView.as_view(), name='address_view'),
    path('address/<int:pk>', views.CustomerAddressDeleteView.as_view(), name='delete_address'),
    path('edit-address/<int:pk>', views.CustomerAddressUpdateView.as_view(), name='edit_address'),
    path('new-address/', views.CustomerAddressCreateView.as_view(), name='new_address'),
]