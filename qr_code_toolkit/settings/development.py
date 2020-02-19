from qr_code_toolkit.settings.base import *

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
