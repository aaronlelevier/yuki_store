"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path 
BASE_DIR = Path(__file__).ancestor(2)

TEMPLATE_DIRS = (
    BASE_DIR.child('templates'),
    BASE_DIR.child('image'),
    )

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
    BASE_DIR.child('media'),
    )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.core.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.request',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
# )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x0=r!3a%w95e0hicv)e_q$k1by2!cq=3zdsl86ve)e!lyqwi+)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'crispy_forms',
    'floppyforms',
    'products',
    # 'paypal_express_checkout',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store',
        'USER': os.environ['MySQL_USER'],
        'PASSWORD': os.environ['MySQL_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'read_default_file': 'my.cnf',
            "init_command": "SET foreign_key_checks = 0;", # use for testing only?
            }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

# STATIC_ROOT = BASE_DIR.child('static') 
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR.child('media') 
MEDIA_URL = '/media/'

# Rackspace EMAIL Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Paypal Settings
# PAYPAL_API_URL = 'https://api-3t.sandbox.paypal.com/nvp'
# PAYPAL_LOGIN_URL = (
#     'https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token='
# )
# SALE_DESCRIPTION = 'Your payment to Foobar Inc.'


# Speed up Tests Settings (also add any hashing algorithm used in fixtures)
# PASSWORD_HASHERS = (
#     'django.contrib.auth.hashers.MD5PasswordHasher',
# )