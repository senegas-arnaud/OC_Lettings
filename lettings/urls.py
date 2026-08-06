"""
URLs de l'application lettings.

Définit les routes de l'application, sous le namespace 'lettings' :
la liste des locations et le détail d'une location spécifique.
"""

from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
