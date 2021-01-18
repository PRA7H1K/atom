from django.urls import path
from .views import home, createShortURL, page_redirect, registerPage, loginPage

urlpatterns = [
    path('', home, name='home'),
    path('create', createShortURL, name='new'),
    path('<str:url>', page_redirect, name='redirect'),
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
]