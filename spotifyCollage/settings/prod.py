from spotifyCollage.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.example.com']

# LOGIN_REDIRECT_URL = '/display_collage'
LOGIN_REDIRECT_URL = 'http://localhost:3000/'

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# CSRF
CSRF_COOKIE_SECURE = True