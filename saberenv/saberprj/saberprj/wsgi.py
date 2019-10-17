"""
WSGI config for saberprj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.core.wsgi import get_wsgi_application

from django.views import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saberprj.settings")

application = get_wsgi_application()