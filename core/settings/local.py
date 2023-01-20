from core.settings import BASE_DIR

DEBUG=True

ALLOWED_HOSTS = [
    "*"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'