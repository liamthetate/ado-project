from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ view for all prudcts and sorting and searhing queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)