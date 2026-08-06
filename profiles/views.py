"""
Vues de l'application profiles.

Ce module gère l'affichage de la liste des profils utilisateurs
et le détail de chacun d'entre eux.
"""

import logging

from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de tous les profils utilisateurs.

    :param request: la requête HTTP entrante.
    :type request: django.http.HttpRequest
    :returns: la page HTML listant tous les profils.
    :rtype: django.http.HttpResponse
    """
    profiles_list = Profile.objects.all()
    logger.info('Profiles index consulted, %d profile(s) found', profiles_list.count())
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche le détail d'un profil utilisateur spécifique.

    :param request: la requête HTTP entrante.
    :type request: django.http.HttpRequest
    :param username: le nom d'utilisateur du profil à afficher,
        extrait de l'URL.
    :type username: str
    :returns: la page HTML affichant le détail du profil demandé.
    :rtype: django.http.HttpResponse
    :raises django.http.Http404: si aucun profil ne correspond
        au nom d'utilisateur fourni.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
    except Exception:
        logger.warning('Profile with username=%s not found', username)
        raise
    logger.info('Profile detail consulted: username=%s', username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
