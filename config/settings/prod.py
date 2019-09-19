# -*- coding: utf-8 -*-
"""`config.settings.prod` module.

Production settings module.
"""


from .base import *


DEBUG = False

# local database for development end testing
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.db.backends.postgresql',
        'NAME': 'pegneon_db',
        'USER': 'pegneon_admin',
        'PASSWORD': '<production-password>',
        'HOST': '<production-host>',
        'PORT': '<production-port>',
    }
}

