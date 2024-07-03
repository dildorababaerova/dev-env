from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields= ['username', 'password']

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


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model= User
        fields= (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


        # first_name= forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Syötä oma etunimesi",

        #         }
        #     )
        # )

        # last_name= forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Syötä oma sukunimesi",

        #         }
        #     )
        # )

        # last_name= forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Syötä oma sukunimesi",

        #         }
        #     )
        # )

        # username= forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Syötä käyttäjätunnus",

        #         }
        #     )
        # )

        # email= forms.CharField(
        #     widget=forms.EmailInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Syötä sähköpostiosoitesi",

        #         }
        #     )
        # )

        # password1= forms.CharField(
        #     widget=forms.PasswordInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Syötä salasanasi",

        #         }
        #     )
        # )

        # last_name= forms.CharField(
        #     widget=forms.PasswordInput(
        #         attrs={
        #             "class": "form-control",
        #             "placeholder": "Vahvista salasanasi",

        #         }
        #     )
        # )

        