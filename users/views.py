from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password )
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Olet kirjoittanut sisään")

                redirect_page= request.POST.get('next', None)

                if redirect_page and redirect_page!=reverse('users:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title':'Savesta-Kirjaudu sisään',
        'form' : form
    }
    
    return render(request, 'users/login.html', context)

    

def registration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Olet luonut tilisi ja kirjoittanut sisään")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
        
    context={
        'title':'Etusivu-Registiröityminen',
        'form' : form
    }
   
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data = request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Olet uusittanut omaprofiilisi")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
        
    context={
        'title':'Etusivu-Oma sivu',
        'form' : form
    }
   
    return render(request, 'users/profile.html', context)



@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Olet kirjoittanut ulos")
    auth.logout(request)
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')


