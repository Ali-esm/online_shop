from django.urls import path
from . import apis, views

app_name = 'order'
urlpatterns = [
    path('delete-product/', views.DeleteProductFromCookieView.as_view(), name='delete_product'),
    path('add-product/', views.AddProductCookieView.as_view(), name='add_product'),
    path('get-products/', apis.GetProductCookieAPIView.as_view(), name='get_products'),
]
