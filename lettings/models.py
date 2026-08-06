"""
Modèles de l'application lettings.

Ce module définit les modèles Address et Letting, représentant
respectivement une adresse postale et une location immobilière
disponible à la réservation.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse postale associée à une location.

    :ivar number: le numéro de rue (entre 0 et 9999).
    :vartype number: int
    :ivar street: le nom de la rue.
    :vartype street: str
    :ivar city: la ville.
    :vartype city: str
    :ivar state: le code de l'état/région (2 caractères minimum).
    :vartype state: str
    :ivar zip_code: le code postal (entre 0 et 99999).
    :vartype zip_code: int
    :ivar country_iso_code: le code ISO du pays (3 caractères minimum).
    :vartype country_iso_code: str
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Options de configuration du modèle Address."""

        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Retourne la représentation textuelle de l'adresse.

        :returns: le numéro et le nom de la rue.
        :rtype: str
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Représente une location immobilière disponible à la réservation.

    :ivar title: le titre ou nom donné à la location.
    :vartype title: str
    :ivar address: l'adresse associée à cette location, en relation
        one-to-one avec le modèle Address.
    :vartype address: lettings.models.Address
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne la représentation textuelle de la location.

        :returns: le titre de la location.
        :rtype: str
        """
        return self.title
