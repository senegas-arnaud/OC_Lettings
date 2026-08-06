"""
URLs de l'application profiles.

Définit les routes de l'application, sous le namespace 'profiles' :
la liste des profils et le détail d'un profil spécifique.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
