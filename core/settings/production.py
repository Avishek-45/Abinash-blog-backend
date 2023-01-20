from core.settings import BASE_DIR
import os

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOST').split(',')

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
    }
}

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"