from django.urls import path
from . import apis, views

app_name = 'order'
urlpatterns = [
    path('', apis.OrderListAPIView.as_view(), name='order_list'),
    path('order-item/', apis.OrderItemListAPIView.as_view(), name='orderitem_list'),
    path('add-to-cart/', views.AddProductCookieView.as_view(), name='add_to_cart_view'),
    path('get-products/', apis.GetProductCookieAPIView.as_view(), name='get_products'),
]
