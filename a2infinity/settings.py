"""
Django settings for a2infinity project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)


# for django ORM to work in jupyter
# https://stackoverflow.com/a/62119475
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# During launch jupyter notebook server will show the address and port and token
# that you will need to use as URL to access it.

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888'
]

BOOTSTRAP4 = {
    'set_placeholder': False,
    'required_css_class': 'required_fields',
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd)qx_w%-pbqhm04n$z(_wc%!!=u$&g2ht+3%*qb68ck(o6q_0w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ["https://a2infinte.herokuapp.com/","192.168.29.158", "127.0.0.1"]

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'home.apps.HomeConfig',
    'django_extensions',
    'users',
    'bootstrap4',
    'crispy_forms'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    #'a2infinity.external_config.custom_middleware.request_exposure.RequestExposerMiddleware', #<--- will set the exposed_request  variable, initiall define it as None
    #'a2infinity.external_config.custom_middleware.request_logging.middleware.LoggingMiddleware', #<--- Added install djang-request-logging
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'a2infinity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + "/templates/html/",BASE_DIR + "/templates/base/"],
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

WSGI_APPLICATION = 'a2infinity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# SECURITY WARNING: don't run with debug turned on in production!
try:
    if os.environ['POSTGRES_REMOTE'] == "0":
        print(os.environ['POSTGRES_REMOTE'])
        HOST_PG = "postgresql"
        print(os.environ['POSTGRES_REMOTE'])
        print(HOST_PG)
    else:
        HOST_PG = "13.232.118.146"
        print(os.environ['POSTGRES_REMOTE'])
        print(HOST_PG)
except:
    HOST_PG = "localhost"
    

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres_bhavya', # should also match MYSQL_DATABASE in dockercompose
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': HOST_PG,   # Or an IP Address that your DB is hosted on
        'PORT': '5432'
    }    
}

print(DATABASES)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR + "/static",
    
]

###-------------------------------###


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'test.otp37@gmail.com'
EMAIL_HOST_PASSWORD = 'newschool'
EMAIL_USE_TLS = True


PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))

if os.path.exists(os.path.join(PROJECT_HOME, "external_config", "api_local_settings.py")):
    from .external_config.api_local_settings import *