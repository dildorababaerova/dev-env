from django.shortcuts import render


def index(request):

    
    context = {
        'title': 'Savesta -Etusivu',
        'content': 'SAVESTA',
        
        }
    return render(request, 'main/index.html', context) 

def about(request):
    context = {
        'title': 'Meidän historia',
        'content': 'Meidän historia',
        'content_text': 'Meidän historia on pitkä ja monivaiheinen. Olemme tehneet tuotteita jo vuodesta 1999.',
    }
    return render(request, 'main/about.html', context)  
