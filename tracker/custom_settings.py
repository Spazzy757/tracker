import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MEDIA_URL = '/media/'
STATIC_ROOT = './static/'
STATIC_URL = '/static/'
if os.environ.get('ENVIRONMENT') is not None:
    STATIC_URL = 'http://165.227.188.79:7072/static/'
