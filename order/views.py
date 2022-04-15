import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem
from product.models import Product
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
        session_items = request.session.items()
        products = dict(filter(lambda k: k[0].startswith('p'), session_items))
        order, created = Order.objects.get_or_create(status__exact='U',
                                                     customer=customer,
                                                     address=customer.address_set.first())
        if created:
            if products:
                for key, value in products.items():
                    product = Product.objects.get(id=int(key[1]))
                    OrderItem.objects.create(order=order, product=product, quantity=int(value))
        else:
            for key, value in products.items():
                product = Product.objects.get(id=int(key[1]))
                order: Order
                if not order.orderitem_set.filter(product=product).exists():
                    OrderItem.objects.create(order=order, product=product, quantity=int(value))

        order_form = OrderForm(instance=order)
        addresses = customer.address_set.all()
        items = []
        for item in order.orderitem_set.all():
            items.append((OrderItemForm(instance=item), item))
        context = {
            'order': order,
            'order_form': order_form,
            'addresses': addresses,
            'items': items,
        }
        res = render(request, 'order/order_items.html', context=context)
        return res
