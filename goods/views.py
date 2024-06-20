from django.shortcuts import render
from .models import Product

def catalog(request):

    goods = Product.objects.all()
    context = {
        'title': 'Etusivu-Catalog',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug=False, product_id=False):

    if product_id:
        product = Product.objects.get(id=product_id)
    else:
        product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    
    return render(request, 'goods/product.html', context=context)

