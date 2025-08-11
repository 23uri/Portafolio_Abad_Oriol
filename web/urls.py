# web/urls.py
from django.urls import path
from . import views  # Importamos las funciones desde views.py

urlpatterns = [
    path('', views.inicio, name='inicio'),  # http://localhost:8000/
    path('quien-soy/', views.quien_soy, name='quien_soy'),  # http://localhost:8000/quien-soy/
    path('contacto/', views.contacto, name='contacto'),  # http://localhost:8000/contacto/
]
