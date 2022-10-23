from spotifyCollage.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['.example.com', 'localhost', 'ancient-stream-51201.herokuapp.com']

# LOGIN_REDIRECT_URL = '/display_collage'
LOGIN_REDIRECT_URL = 'http://localhost:3000/'


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

