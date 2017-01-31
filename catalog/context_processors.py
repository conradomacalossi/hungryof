from .models import Category

from .models import Product, Category

def categories(request):

    return {
        'categories': Category.objects.all()
    }

def products(request):

    return {
        'products': Product.objects.all()
    }
