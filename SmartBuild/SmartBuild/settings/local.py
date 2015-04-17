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
