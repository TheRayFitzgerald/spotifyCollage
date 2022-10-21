from spotifyCollage.settings.base import *
import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.example.com', 'localhost', 'ancient-stream-51201.herokuapp.com']

# LOGIN_REDIRECT_URL = '/display_collage'
LOGIN_REDIRECT_URL = 'http://localhost:3000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'd43cod7f55p4bk',
        'USER': 'qkfrtsaysebktb',
        'PASSWORD': '97934df4d8acbbe5a0796ec11dd09fe9aa21bdb818ca58e4f07281aa717d8fb1',
        'HOST': 'ec2-18-208-55-135.compute-1.amazonaws.com', 
        'PORT': '5432',                  
    }
}



# SECURITY SETTINGS

SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# CSRF
CSRF_COOKIE_SECURE = False

# statticfiles STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 

django_heroku.settings(locals())