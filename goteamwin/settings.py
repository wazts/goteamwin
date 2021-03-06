"""
Django settings for goteamwin project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '#c0!toy%eolv1_ik=j193%27cghp!+i@l+2fy$m&wx5*b$)x8r')

# SECURITY WARNING: don't run with debug turned on in production!
RUN_MODE = os.getenv('RUN_MODE', 'development')

DEBUG = False
if (RUN_MODE == 'development' or RUN_MODE == 'staging'):
    DEBUG=True
    
DEBUG = os.getenv('DEBUG', DEBUG)

# --- Change the default behaviour of the toolbar

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : lambda x: DEBUG,
}

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS','')]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'debug_toolbar',
    
    'taggit',
    'storages',
    'polymorphic',
    'embed_video',
    
    # Apps
    'goteamwin',
    'post',
    'series',
    'textPost',
    'video'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'goteamwin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'goteamwin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {}
if RUN_MODE == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
    
    # Enable Connection Pooling
    DATABASES['default']['ENGINE'] = 'django_postgrespool'


# --- Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# --- Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles'
STATIC_URL = BASE_DIR + '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

if DEBUG:
    WHITENOISE_MAX_AGE = 60
else:
    WHITENOISE_MAX_AGE = 604800
   
  
# --- Image storage 
if RUN_MODE == 'staging':
    COMIC_STORAGE = 'staging'
else:
    COMIC_STORAGE='comics'

if RUN_MODE != 'development':
    AWS_HEADERS = {
        'Expires': 'Wed, 1 Jan 2020 00:00:00 CST',
        'Cache-Control': 'max-age=1209600',
    }
    AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
    AWS_S3_SECURE_URLS = os.getenv('AWS_S3_SECURE_URLS', False)
    AWS_QUERYSTRING_AUTH = os.getenv('AWS_QUERYSTRING_AUTH', False)
    
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    
    MEDIA_URL = 'http://%s/' % AWS_S3_CUSTOM_DOMAIN
    MEDIA_ROOT  = MEDIA_URL

else:
    MEDIA_URL='/media/'
    MEDIA_ROOT=BASE_DIR
    
# SITE INFO
SITE_NAME = os.getenv('SITE_NAME', 'Your Site Name')

# PAGINATION
PAGINATION_LIMIT = 10
