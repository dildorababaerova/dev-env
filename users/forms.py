from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()
       
    # username = forms.CharField(
    #     label= 'Käyttäjän nimi',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                                         'class':"form-control", 
    #                                                         'placeholder': "Kirjoita oma nimesi"})
    # )
    # password = forms.CharField(
    #     label= 'Salasana',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                         'class':"form-control", 
    #                                         'placeholder': "Kirjoita salasanasi"})
    # )
    
    class Meta:
        model = User
        fields= ['username', 'password']