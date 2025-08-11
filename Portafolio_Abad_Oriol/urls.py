# Portafolio_Abad_Oriol/urls.py
from django.contrib import admin
from django.urls import path, include  # <-- ¡Importante!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),  # <-- Redirige a las URLs de la app web
]
