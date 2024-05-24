"""
WSGI config for Diminuendo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Diminuendo.settings')

SECRET_KEY = "725jl%5*3p9ep_we1#5n5*fn90r#+r)d@k#(h1@d(wo51r#hkb"

application = get_wsgi_application()
