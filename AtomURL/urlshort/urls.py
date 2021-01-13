from django.urls import path
from .views import home, createShortURL, redirect, registerPage, loginPage

urlpatterns = [
    path('', home, name='home'),
    path('create', createShortURL, name='create'),
    path('<str:url>', redirect, name='redirect'),
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
]