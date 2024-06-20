from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from .models import Product

def catalog(request, category_slug, page=1):
    if category_slug == 'kaikki-tuotteet':
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Etusivu-Catalog',
        'goods': current_page,
        'slug-url': category_slug
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

