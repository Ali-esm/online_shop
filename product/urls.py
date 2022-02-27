from django.urls import path
from .views import ProductListView, HotProductView, ProductDetailView

app_name = 'product'
urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]