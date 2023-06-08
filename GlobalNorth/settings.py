"""
Django settings for GlobalNorth project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config
import ast


# config = Config(RepositoryEnv(".env"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if 'RDS_DB_NAME' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
    ALLOWED_HOSTS = ['theglobalnorth.com']
else:
    SECRET_KEY = config('SECRET_KEY')
    # DEBUG = bool(int(os.getenv('DEBUG')))
    host = os.getenv('ALLOWED_HOST')
    # ALLOWED_HOSTS =  ast.literal_eval(host)
    ALLOWED_HOSTS = ['127.0.0.1','localhost','*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'import_export',
    'tinymce',
    'storages',

    'accounts.apps.AccountsConfig',
    'home.apps.HomeConfig',
    'services.apps.ServicesConfig',
    'Payment.apps.PaymentConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GlobalNorth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'GlobalNorth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "accounts.User"
PROJECT_TITLE = "The Global North"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
 }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kevinopix@gmail.com'
EMAIL_HOST_PASSWORD = 'qvuukjiawrjdsncg'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ADMINS = [("kevinopix", EMAIL_HOST_USER),]


if DEBUG:
    EMAIL_SETUP_DOMAIN = '127.0.0.1:8000'
    EMAIL_SETUP_SITENAME = 'The Global North'
    EMAIL_SETUP_PROTOCOL = 'http'
    STRIPE_PUBLISHABLE_KEY = config("STRIPE_TEST_PUBLISHABLE_KEY")
    STRIPE_SECRET_KEY = config("STRIPE_TEST_SECRET_KEY")
    DOMAIN_URL = 'http://127.0.0.1:8000'
    STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")
else:
    EMAIL_SETUP_DOMAIN = '127.0.0.1:8000'
    EMAIL_SETUP_SITENAME = 'The Global North'
    EMAIL_SETUP_PROTOCOL = 'http'
    DOMAIN_URL = 'http://127.0.0.1:8000'


if 'STRIPE_PROD_PUBLISHABLE_KEY' in os.environ:
    STRIPE_WEBHOOK_SECRET = os.environ["STRIPE_PROD_WEBHOOK_SECRET"]
    STRIPE_PUBLISHABLE_KEY = os.environ["STRIPE_PROD_PUBLISHABLE_KEY"]
    STRIPE_SECRET_KEY = os.environ["STRIPE_PROD_SECRET_KEY"]
    DOMAIN_URL = 'https://theglobalnorth.com'
    DEBUG = bool(int(os.environ["DEBUG_VALUE"]))
    CSRF_TRUSTED_ORIGINS = ['https://theglobalnorth.com']




if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']

    AWS_S3_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    SECURE_SSL_REDIRECT = True


PAYMENT_CANCEL_URL = DOMAIN_URL + "/pay/cancel/"
PAYMENT_SUCCESS_URL = DOMAIN_URL + "/pay/success/"