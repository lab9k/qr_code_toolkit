from qr_code_toolkit.settings.base import *
import django_heroku

django_heroku.settings(locals())

DEBUG = False
ALLOWED_HOSTS = ['qrcodetoolkit.herokuapp.com', 'generic-qr-code-toolkit.herokuapp.com',
                 'hungry-swanson-3696fc.netlify.com']
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
DEBUG_TOOLBAR_PATCH_SETTINGS = False

_index = INSTALLED_APPS.index('django.contrib.staticfiles')
[INSTALLED_APPS.insert(_index + 1, x) for x in ['cloudinary',
                                                'cloudinary_storage']]
