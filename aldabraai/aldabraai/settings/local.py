"""
 LOCAL SETTINGS FILE FOR ALDABRA.AI
 WARNING: THIS SHOULD NOT BE USED IN PRODUCTION MODELS
 WARNING: ONLY USE IN DEVELOPMENT

 TO DISABLE THIS SETTINGS: SET 'live=True' IN './__init__' file
"""

from .base import *

DEBUG = True

SECRET_KEY = '@fats@v7c5ss%#z8rx801@*zqpjy16_zap5hl+kwjv6qkvo$*k'

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = [
    '0.0.0.0', 
    '127.0.0.1'
    ]

DATABASES = {

    ### PROPOSED LOCAL DATABASE
    ### COMMENT OUT PREFERED CHOICE
    ### AND INPUT REQUIRED CHOICE  
    
    ## MySQL

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     },
    # }

    ## postgreSQL

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'aldabradb',

        'USER': 'krummitz',

        'PASSWORD': 'passcodepglocaladmin',

        'HOST': '',

        'PORT': '5432',
    }

}

SHARE_URL = "http://127.0.0.1:8000"

# Static assets
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)
# User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')



## EMAIL SERVICES
EMAIL_HOST = '******'
EMAIL_PORT = '******'
EMAIL_USE_SSL = '******'
EMAIL_HOST_USER = '******'
EMAIL_HOST_PASSWORD = '******'