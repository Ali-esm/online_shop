from django.views import generic
from django.shortcuts import render
from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = "product/product-list.html"
    context_object_name = "products"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        category = request.GET.get("category", None)
        if category:
            context = {"products": Product.objects.filter(category__name=category)}
            return render(request, "product/product-list.html", context=context)
        return super().get(request, *args, **kwargs)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/product-detail.html"


class HotProductView(generic.ListView):
    model = Product
    template_name = "product/landing.html"
    context_object_name = "products"
    queryset = Product.objects.all().order_by("-id")[:6]
