from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Homepage accessed')
    return render(request, 'index.html')
