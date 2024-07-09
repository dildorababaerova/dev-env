from django import template
from django.utils.http import urlencode

from goods.models import Category



register = template.Library()

@register.simple_tag
def tag_category():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def change_param(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)






