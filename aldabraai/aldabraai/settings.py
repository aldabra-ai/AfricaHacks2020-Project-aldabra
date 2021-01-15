"""
Django settings for aldabraai project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@fats@v7c5ss%#z8rx801@*zqpjy16_zap5hl+kwjv6qkvo$*k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = [
    ## DJANGO CORE(s)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## OWN APP(s) 
    # AUTH END
    'authend.apps.AuthendConfig',
    # COMMON
    'base.apps.BaseConfig',
    'accounts.apps.AccountsConfig',
    'hospitaldb.apps.HospitaldbConfig',
    # FEATURE(s)
    'dashboard.apps.DashboardConfig',
    'appointment.apps.AppointmentConfig',
    'queuein.apps.QueueinConfig',
    'mhealth.apps.MhealthConfig',
    'search.apps.SearchConfig',
    # FRONT END
    'frontend.apps.FrontendConfig',

    ## API FRAMEWORK
    'rest_framework',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

## REFRENCING USER MODEL
AUTH_USER_MODEL = 'authend.User'

## ROOT URL
ROOT_URLCONF = 'aldabraai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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
\
WSGI_APPLICATION = 'aldabraai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # SQLite3

    'dev-fallback': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    # MySQL

    # 'dev-database': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     },
    # }

    # postgreSQL

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'aldabradb',

        'USER': 'krummitz',

        'PASSWORD': 'passcodepglocaladmin',

        'HOST': '',

        'PORT': '5432',
    }

}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# PRODUCTION
# MEDIA_ROOT = '' 


# DEVELOPMENT
#MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

