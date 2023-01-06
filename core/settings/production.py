from core.settings import BASE_DIR

ALLOWED_HOSTS = [
    "abinashapi.avishekguragain.com.np"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}