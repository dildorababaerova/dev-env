from django.http import JsonResponse
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Product




def cart_add(request):

    product_id = request.POST.get("product_id")
    product= Product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product )

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            cart = Cart.objects.create(user=request.user, product=product, quantity=1)
    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = { 
        "message": "Tuote lisätty ostoskoriin",
        "cart_items_html": cart_items_html,
    }


    return JsonResponse(response_data)



def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = int(request.POST.get("quantity"))
    cart= Cart.objects.get(id=cart_id)
    cart.quantity= quantity
    cart.save()
    updated_quantity = cart.quantity
    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = { 
        "message": "Tuote poistettu",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }


    return JsonResponse(response_data)

    

    

def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    cart= Cart.objects.get(id=cart_id)
    quantity= cart.quantity
    cart.delete()
    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = { 
        "message": "Tuote poistettu",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }


    return JsonResponse(response_data)

    
