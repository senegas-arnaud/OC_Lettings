"""
Vues de l'application oc_lettings_site.

Ce module gère l'affichage de la page d'accueil générale du site.
"""

import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la page d'accueil du site.

    :param request: la requête HTTP entrante.
    :type request: django.http.HttpRequest
    :returns: la page HTML d'accueil.
    :rtype: django.http.HttpResponse
    """
    logger.info('Homepage accessed')
    return render(request, 'index.html')
