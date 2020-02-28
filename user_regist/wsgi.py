"""
WSGI config for user_regist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_regist.settings')
# sys.path.append('/var/www//django-apps/source/event_organizer')
# sys.path.append('/var/www//django-apps/source/event_organizer/user_regist')

paths = [
    '/var/www//django-apps/source/event_organizer',
    '/var/www//django-apps/source/event_organizer/user_regist',
    '/var/www//django-apps/env/lib/python3.6/site-packages',
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)


application = get_wsgi_application()
