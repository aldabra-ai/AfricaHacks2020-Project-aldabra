"""
Django settings for aldabraai project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uerqa6=r+@+3cjgt+rb93btugo944n_sjezj+h8%wz36d3)-@n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # own apps
    'baseapp.apps.BaseappConfig',
    'hospitaldb.apps.HospitaldbConfig',
    'patient.apps.PatientConfig',
    'rest_framework',

    # corsheaders
    'corsheaders',
]

MIDDLEWARE = [
    # cors
    'corsheaders.middleware.CorsMiddleware',

    # Defaults
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = ['https://localhost:3000']

ROOT_URLCONF = 'aldabraai.urls'

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
        },
    },
]

WSGI_APPLICATION = 'aldabraai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
   #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
      #  },

      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aldabraai',
        'USER': 'aldabraadmin',
        'PASSWORD': 'aldabradb',
        'HOST': 'mysql-16530-0.cloudclusters.net',
        'PORT': 16530,
        #'OPTIONS': {
         #   'read_default_file': '/etc/mysql/my.cnf',
        #},
      }

    #  'default': {
    #         'ENGINE': 'djongo',
    #         'NAME': 'aldabracluster',
    #         'ENFORCE_SCHEMA': False,
    #         'CLIENT': {
    #             'host': 'mongodb+srv://aldabraai:passcodealdabraaidb@aldabracluster.57cqg.mongodb.net/aldabracluster?retryWrites=true&w=majority',
    #             'port': 27017,
    #             'username': 'aldabraai',
    #             'password': 'passcodealdabraaidb',
    #             'authSource': 'aldabracluster',
    #             'authMechanism': 'SCRAM-SHA-1'
    #         },

    #         'LOGGING': {
    #             'version': 1,
    #             'loggers': {
    #                 'djongo': {
    #                     'level': 'DEBUG',
    #                     'propagate': False,                        
    #                 }
    #             },
    #          },

    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
