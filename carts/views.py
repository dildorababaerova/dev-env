from django.shortcuts import redirect


from carts.models import Cart
from goods.models import Product


def cart_add(request, product_slug):
    product= Product.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(product=product, user=request.user)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
    else:
        cart = Cart.objects.create(product=product, user=request.user, quantity=1)

        

    return redirect(request.META.get('HTTP_REFERER'))


def cart_change(request, product_slug):
    ...

def cart_remove(request):
    ...
