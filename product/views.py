from django.views import generic
from django.shortcuts import render
from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'
    paginate_by = 15


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product-detail.html'


class HotProductView(generic.ListView):
    model = Product
    template_name = 'product/landing.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:3]
