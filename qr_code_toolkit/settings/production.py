from qr_code_toolkit.settings.base import *

DEBUG_TOOLBAR_PATCH_SETTINGS = False

import django_heroku

django_heroku.settings(locals())
