from .base_settings import *

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES[0]['DIRS'].append("/src/app/templates")


def get_secret(key, default=False):
    value = os.environ.get(key)
    if value:
        return value.strip()
    try:
        f = open("/run/secrets/%s" % key)
    except OSError as e:
        return default
    value = f.read()
    f.close()
    return value.strip()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASS'),
        'HOST': get_secret('DB_HOST'),
        'PORT': '',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

STATIC_ROOT = '/static'

EMAIL_HOST = get_secret('EMAIL_HOST')
EMAIL_HOST_USER = get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
EMAIL_FAKE = get_secret('EMAIL_FAKE')

if get_secret('DEBUG'):
    DEBUG = True
