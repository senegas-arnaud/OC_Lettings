
from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    lettings_list = Letting.objects.all()
    logger.info('Lettings index consulted, %d letting(s) found', lettings_list.count())
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
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
