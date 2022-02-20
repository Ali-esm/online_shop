from django.urls import path
from.views import CustomerLoginView, CustomerSignUpView, CustomerLogoutView

app_name = 'customer'
urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login_view'),
    path('signup/', CustomerSignUpView.as_view(), name='signup_view'),
    path('logout/', CustomerLogoutView.as_view(), name='logout_view'),
]