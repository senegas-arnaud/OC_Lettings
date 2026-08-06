"""
Configuration de l'interface d'administration pour l'application profiles.

Enregistre le modèle Profile dans l'admin Django,
avec la configuration par défaut.
"""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
