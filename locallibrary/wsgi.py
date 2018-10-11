"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/admin/locallibrary/locallibrary')

# add the virtualenv site-packages path to the sys.path
sys.path.append('~/.virtualenvs/djangodev/bin/lib/python3.6/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
