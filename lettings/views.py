"""
Vues de l'application lettings.

Ce module gère l'affichage de la liste des locations disponibles
et le détail de chacune d'entre elles.
"""

import logging

from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de toutes les locations disponibles.

    :param request: la requête HTTP entrante.
    :type request: django.http.HttpRequest
    :returns: la page HTML listant toutes les locations.
    :rtype: django.http.HttpResponse
    """
    lettings_list = Letting.objects.all()
    logger.info('Lettings index consulted, %d letting(s) found', lettings_list.count())
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche le détail d'une location spécifique.

    :param request: la requête HTTP entrante.
    :type request: django.http.HttpRequest
    :param letting_id: l'identifiant (clé primaire) de la location
        à afficher, extrait de l'URL.
    :type letting_id: int
    :returns: la page HTML affichant le détail de la location demandée.
    :rtype: django.http.HttpResponse
    :raises django.http.Http404: si aucune location ne correspond
        à l'identifiant fourni.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
    except Exception:
        logger.warning('Letting with id=%s not found', letting_id)
        raise
    logger.info('Letting detail consulted: id=%s, title=%s', letting_id, letting.title)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
