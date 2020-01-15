from qr_code_toolkit.settings.base import *
import django_heroku

django_heroku.settings(locals())

DEBUG = False
ALLOWED_HOSTS = ['qrcodetoolkit.herokuapp.com']
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
DEBUG_TOOLBAR_PATCH_SETTINGS = False
