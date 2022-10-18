from spotifyCollage.settings.base import *
import django_heroku

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.example.com', 'localhost']

# LOGIN_REDIRECT_URL = '/display_collage'
LOGIN_REDIRECT_URL = 'http://localhost:3000/'

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# CSRF
CSRF_COOKIE_SECURE = True

django_heroku.settings(locals())