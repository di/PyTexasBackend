"""
Django settings for pytx project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

ALLOWED_HOSTS = [
    'pallas.neutrondrive.com',
    'pytexas.herokuapp.com',
    'www.pytexas.org',
    'pytexas.org',
    '.pytexas.org',
]

# Application definition

INSTALLED_APPS = [
    'flat_responsive',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djzen',
    'django_uwsgi',
    'storages',
    
    'conference.profiles',
    'conference.event',
    
    'graphene_django',
    'raven.contrib.django.raven_compat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pytx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pytx', 'templates')],
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

WSGI_APPLICATION = 'pytx.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'profiles.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

FRONTEND = '2017-dist'
FRONTEND_DIR = os.environ.get('FRONTEND_DIR', os.path.join(BASE_DIR, 'node_modules', 'pytexas'))
FRONTEND_TEMPLATES = os.path.join(FRONTEND_DIR, 'app')
FRONTEND_MD = os.path.join(FRONTEND_DIR, 'app', 'md')

STATIC_URL = '/static-2017/'

STATIC_ROOT = os.path.join(BASE_DIR, "static-compiled")

# Uncomment for forever-cacheable files and compression support
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    FRONTEND_DIR,
    os.path.join(BASE_DIR, 'frontend'),
    os.path.join(BASE_DIR, 'node_modules', 'vue', 'dist'),
    os.path.join(BASE_DIR, 'node_modules', 'vue-router', 'dist'),
    os.path.join(BASE_DIR, 'node_modules', 'vue-material', 'dist'),
    os.path.join(BASE_DIR, "node_modules", "md-icons"),
    os.path.join(BASE_DIR, "node_modules", "roboto-fontface", "fonts",
                 "roboto"),
    os.path.join(BASE_DIR, "node_modules", "roboto-fontface", "fonts",
                 "roboto-slab"),
    os.path.join(BASE_DIR, "node_modules", "axios", "dist"),
    os.path.join(BASE_DIR, "node_modules", "showdown", "dist"),
    os.path.join(BASE_DIR, 'node_modules', 'raven-js', 'dist'),
]

# Uncomment if using Heroku
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTH_USER_MODEL = 'profiles.User'

GRAPHENE = {'SCHEMA': 'pytx.schema.schema'}

CURRENT_CONF = '2017'

STRIPE_PUB_KEY = os.environ.get('STRIPE_PUB_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')

SERVER_EMAIL = 'conference@pytexas.org'
DEFAULT_FROM_EMAIL = 'conference@pytexas.org'

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('AWS_ACCESS_KEY', '')
EMAIL_HOST_PASSWORD = os.environ.get('AWS_SECRET_KEY', '')
EMAIL_USE_TLS = True


from pytx.settings.logging import *
