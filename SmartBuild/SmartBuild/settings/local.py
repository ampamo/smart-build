# -*- encoding: utf-8 -*-
#import os
#from ._base import BASE_DIR

from ._base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT  = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
STATIC_URL  = '/static/'
MEDIA_URL   = '/media/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
