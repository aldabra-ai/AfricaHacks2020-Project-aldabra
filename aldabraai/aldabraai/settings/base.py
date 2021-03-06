
import os

import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from django.core.exceptions import ImproperlyConfigured

with open('secrets.json') as file:
    secrets = json.loads(file.read())   

    
def get_variable_or_secrete(var_or_setting, secrets=secrets, limit_to_secret=False):
    if limit_to_secret:
        try:
            return secrets[var_or_setting]
        except KeyError:
            error_msg = f'No secret named {var_or_setting}'
            raise ImproperlyConfigured(error_msg)
            
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_or_setting]
    except KeyError:
        print('***Unable to get environmental variable...\nTrying somethig else...***')
       
        try:
            return secrets[var_or_setting]     
        except KeyError:
            error_msg = f'Set the {var_or_setting} environment variable'
            raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_variable_or_secrete('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool

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
    'account.apps.AccountConfig',
    'hospitaldb.apps.HospitaldbConfig',

    # FEATURE(s)
    'dashboard.apps.DashboardConfig',
    'appointment.apps.AppointmentConfig',
    'queuein.apps.QueueinConfig',
    'mhealth.apps.MhealthConfig',
    'search.apps.SearchConfig',

    # FRONT END
    'frontend.apps.FrontendConfig',

    ## THIRD PARTY APPS
    # API FRAMEWORK
    'rest_framework',

    # AUTHORIZATION LIBRARY
    'knox',


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
    # # SQLite3

    # 'dev-fallback': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },   
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


MEDIA_URL = '/media/'

STATIC_URL = '/static/'




## Authentication Settings
# Backend



## EMAIL SERVICES
EMAIL_HOST = '******'
EMAIL_PORT = '******'
EMAIL_USE_SSL = '******'
EMAIL_HOST_USER = '******'
EMAIL_HOST_PASSWORD = '******'

REST_FRAMEWORK = {

    'TEST_REQUEST_DEFAULT_FORMAT': 'json', 

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
         #'rest_framework.authentication.BasicAuthentication',
         #'rest_framework.authentication.SessionAuthentication',
         #'rest_framework.authentication.TokenAuthentication',
     ],

}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'