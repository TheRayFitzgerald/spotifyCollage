from spotifyCollage.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['.example.com', 'localhost', 'ancient-stream-51201.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'spotifyCollage',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1', 
        'PORT': '5432',                  
    }
}

