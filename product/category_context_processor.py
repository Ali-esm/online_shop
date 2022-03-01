from .models import Category


def category_render(request):
    return {
        'categories': Category.objects.all(),
        'sub_categories': Category.objects.filter(is_sub=True),
        'root_categories': Category.objects.filter(is_sub=False),
    }