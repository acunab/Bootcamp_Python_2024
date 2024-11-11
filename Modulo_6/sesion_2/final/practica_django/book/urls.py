from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal de Book que hace referencia a la vista index
]