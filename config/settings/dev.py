# -*- coding: utf-8 -*-
"""`config.settings.dev` module.

Production settings module.
"""


from .base import *

DEBUG = True

# local database for development end testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pegneon_db',
        'USER': 'pegneon_admin',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}

DEBUG_APPS = [
    'debug_toolbar'
]

INSTALLED_APPS += DEBUG_APPS


MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

