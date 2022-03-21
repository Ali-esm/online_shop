from django.urls import path
from . import apis, views

app_name = 'order'
urlpatterns = [
    path('add-to-cart/', views.AddProductCookieView.as_view(), name='add_to_cart_view'),
    path('get-products/', apis.GetProductCookieAPIView.as_view(), name='get_products'),
]
