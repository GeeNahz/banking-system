from .base_settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'po0172$69b@78ps4v^uhfxu6q--8ko7kpp7rbz420s_3w#sir%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}