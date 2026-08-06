"""
Configuration de l'interface d'administration pour l'application lettings.

Enregistre les modèles Letting et Address dans l'admin Django,
avec la configuration par défaut.
"""

from django.contrib import admin

from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
