from spotifyCollage.settings.base import *

DEBUG = True

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
