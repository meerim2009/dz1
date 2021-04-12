from django.shortcuts import render

# Create your views here.
from test_app.models import Category, Product


def get_all_posts(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    data = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context=data)