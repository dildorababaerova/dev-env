from django.shortcuts import render

from goods.models import Category

def index(request):

    
    context = {
        'title': 'Savesta -Etusivu',
        'content': 'SAVESTASSA TEHTYJÄ TUOTTEITA',
        
        }
    return render(request, 'main/index.html', context) 

def about(request):
    context = {
        'title': 'Meidän historia',
        'content': 'Meidän historia',
        'content_text': 'Meidän historia on pitkä ja monivaiheinen. Olemme tehneet tuotteita jo vuodesta 1999.',
    }
    return render(request, 'main/about.html', context)  
