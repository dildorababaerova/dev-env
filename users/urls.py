from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('users_cart/', views.users_cart, name='users_cart'),
    path('profile/', views.profile, name='profile'),
]   