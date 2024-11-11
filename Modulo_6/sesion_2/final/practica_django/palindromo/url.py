# palindromo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<str:palabra>/', views.es_palindromo, name='es_palindromo'),
]