from spotifyCollage.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', 'ancient-stream-51201.herokuapp.com', '.rayfitzgerald.io']
CORS_ORIGIN_ALLOW_ALL = False

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

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# CSRF
CSRF_COOKIE_SECURE = True

# statticfiles STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
CORS_ORIGIN_ALLOW_ALL = True
'''
CORS_ALLOWED_ORIGINS = [
    "https://www.rayfitzgerald.io",
    "https://rayfitzgerald.io",
    "http://www.rayfitzgerald.io",
    "http://rayfitzgerald.io",
]
'''