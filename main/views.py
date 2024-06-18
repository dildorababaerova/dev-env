from django.shortcuts import render
from django.db.models.manager import BaseManager

from goods.models import Category

def index(request):

    categories = Category.objects.all()
    context = {
        'title': 'Savesta -Etusivu',
        'content': 'SAVESTASSA TEHTYJÄ TUOTTEITA',
        'categories': categories
        }
    return render(request, 'main/index.html', context) 

def about(request):
    context = {
        'title': 'Meidän historia',
        'content': 'Meidän historia',
        'content_text': 'Meidän historia on pitkä ja monivaiheinen. Olemme tehneet tuotteita jo vuodesta 1999.',
    }
    return render(request, 'main/about.html', context)  
