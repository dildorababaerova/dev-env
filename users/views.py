from django.shortcuts import render


def login(request):
    context = {
        'title':'Savesta-Kirjautu sisään'
    }
    
    return render(request, 'users/login.html', context)

    

def registration(request):
    context={
        'title':'Etusivu-Registiröityminen'
    }
   
    return render(request, 'users/registration.html', context)


def logout(request):
    context={
        'title':'Etusivu-Kirjautu ulos'
    }
   
    return render(request, 'users/registration.html', context)


def profile(request):
    context={
        'title':'Etusivu-Oma sivu'
    }
   
    return render(request, 'users/profile.html', context)




