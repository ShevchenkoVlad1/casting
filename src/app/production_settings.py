# -*- coding: utf-8 -*-
from .base_settings import *

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES[0]['DIRS'].append("./src/app/templates")


def get_secret(key):
    value = os.environ.get(key)
    return str(value).strip()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'casting',
        'USER': 'Morethan2019',
        'PASSWORD': 'f571d659ab929d1416e37d55d5165c312b741ad4a82f66fa312bb753e6d5e7ee',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'morethancast@gmail.com'
EMAIL_HOST_PASSWORD = 'Morethan2019'
EMAIL_FAKE = 'no'

if get_secret('DEBUG'):
    DEBUG = True
