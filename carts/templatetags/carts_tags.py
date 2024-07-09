# from carts.utils import get_user_carts
from django import template

from carts.models import Cart
 



register = template.Library()

@register.simple_tag
def user_carts(request):
    # return get_user_carts(request)
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)