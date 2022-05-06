from django.urls import path
from . import apis, views

app_name = 'order'
urlpatterns = [
    path('delete-product/', views.DeleteProductFromCookieView.as_view(), name='delete_product'),
    path('add-product/', views.AddProductCookieView.as_view(), name='add_product'),
    path('get-products/', apis.GetProductCookieAPIView.as_view(), name='get_products'),
    path('items/', views.OrderItemsView.as_view(), name='items_view'),
    path('remove-item/', views.RemoveOrderItem.as_view(), name='remove_item'),
    path('change-status/', views.ChangeOrderStatus.as_view(), name='change_status'),
    path('change-count/', apis.OrderItemCountPartialUpdate.as_view(), name='change_count'),
    path('off-code/', apis.OrderOffCodeAPIView.as_view(), name='submit_offcode'),
]
