from .models import Order


def get_last_n_orders(n):
    orders = Order.objects.all().reverse()[:n]
    return orders
