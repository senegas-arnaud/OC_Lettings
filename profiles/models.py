"""
Modèles de l'application profiles.

Ce module définit le modèle Profile, représentant les informations
de profil associées à un utilisateur Django.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil d'un utilisateur.

    :ivar user: l'utilisateur associé à ce profil, en relation
        one-to-one avec le modèle User de Django.
    :vartype user: django.contrib.auth.models.User
    :ivar favorite_city: la ville favorite de l'utilisateur (facultatif).
    :vartype favorite_city: str
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne la représentation textuelle du profil.

        :returns: le nom d'utilisateur associé au profil.
        :rtype: str
        """
        return self.user.username
