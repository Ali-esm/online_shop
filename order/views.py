import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class AddProductCookieView(View):

    def post(self, request):
        # if user authenticated save to session else save to cookie
        post_body = json.loads(request.body.decode('utf-8'))
        product_id = post_body.get('product', None)
        res = HttpResponse('')
        if product_id:
            quantity = request.POST.get('quantity', 1)
            res.set_cookie(f'p{product_id}', str(quantity))
        return res


class DeleteProductFromCookieView(View):

    def delete(self, request):
        request_body = json.loads(request.body.decode('utf-8'))
        product_id = request_body.get('product', None)
        res = HttpResponse('')
        print(product_id)
        if product_id:
            res.delete_cookie(f'p{product_id}')
        return res
