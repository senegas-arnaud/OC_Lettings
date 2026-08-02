from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    profiles_list = Profile.objects.all()
    logger.info('Profiles index consulted, %d profile(s) found', profiles_list.count())
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    try:
        profile = get_object_or_404(Profile, user__username=username)
    except Exception:
        logger.warning('Profile with username=%s not found', username)
        raise
    logger.info('Profile detail consulted: username=%s', username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
