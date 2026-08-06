"""
URLs principales du projet oc_lettings_site.

Définit la route de la page d'accueil, et inclut les URLs
des applications lettings et profiles ainsi que celles de l'admin.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
