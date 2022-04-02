import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class AddProductCookieView(View):

    def post(self, request):
        post_body = json.loads(request.body.decode('utf-8'))
        product_id = post_body.get('product', None)
        quantity = request.POST.get('quantity', 1)  # this line maybe have problem
        res = HttpResponse('')
        if product_id:
            if request.user.is_authenticated:
                request.session[f'p{product_id}'] = str(quantity)
            else:
                res.set_cookie(f'p{product_id}', str(quantity))
            return res


class DeleteProductFromCookieView(View):

    def delete(self, request):
        request_body = json.loads(request.body.decode('utf-8'))
        product_id = request_body.get('product', None)
        res = HttpResponse('')
        if product_id:
            if request.user.is_authenticated:
                del request.session[f'p{product_id}']
            else:
                res.delete_cookie(f'p{product_id}')
        return res
