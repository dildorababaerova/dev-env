from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   context: dict[str, str] ={
       'title': 'Savesta -Etusivu',
       'content': 'SAVESTASSA TEHTYJÄ TUOTTEITA',
   }
   return render(request, 'main/index.html', context) 

def about(request):
   context: dict[str, str] ={
       'title': 'Meidän historia',
       'content': 'Meidän historia',
       'content_text': 'Meidän historia on pitkä ja monivaiheinen. Olemme tehneet tuotteita jo vuodesta 1999.',
   }
   return render(request, 'main/about.html', context)  
