from .models import Customer


def get_last_n_orders(n: int, customer: Customer):
    orders = customer.orders.all().order_by("-id")[:n]
    return orders
