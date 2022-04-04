import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Order, OrderItem
from customer.models import Customer


class AddProductCookieView(View):

    def post(self, request):
        post_body = json.loads(request.body.decode('utf-8'))
        product_id = post_body.get('product', None)
        quantity = request.POST.get('quantity', 1)  # this line maybe have problem
        res = HttpResponse('')
        if product_id:
            request.session[f'p{product_id}'] = str(quantity)
            return res


class DeleteProductFromCookieView(View):

    def delete(self, request):
        request_body = json.loads(request.body.decode('utf-8'))
        product_id = request_body.get('product', None)
        res = HttpResponse('')
        if product_id:
            del request.session[f'p{product_id}']
        return res


class OrderItemsView(LoginRequiredMixin, View):

    def get(self, request):
        customer = Customer.objects.get(user__phone_number=request.user.phone_number)
        if customer.address_set.count() == 0:
            return redirect(reverse('customer:address_view'))
        products = request.session.items()
        order = Order.get_or_create_order()
        print(products)
        return render(request, 'order/order_items.html')