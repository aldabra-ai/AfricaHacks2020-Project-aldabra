"""
 PRODUCTION SETTINGS FILE FOR ALDABRA.AI
 WARNING: MAKE SURE THE APPOPRIATE SETTINGS AND VAIRIABLES ARE USED ACCORDING TO THOSE PROVIDED BY YOUR HOST PROVIDING SERVICE
 WARNING: ONLY USE IN PRODUCTION

 TO ANABLE THIS SETTINGS: SET 'live=True' IN './__init__' file

"""

from .base import *

DEBUG = False

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = [
    '0.0.0.0'
    ]

DATABASES = {

    ### PROPOSED PRODUCTION DATABASE
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

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',

    #     'NAME': '',

    #     'USER': '',

    #     'PASSWORD': '',

    #     'HOST': '',

    #     'PORT': '5432',
    # }

}

## STATIC ASSETS
# THIS DEPENDS ON THE HOSTING SERVICE ENVIRONMENT 
# MAKE SURE TO GET APPOPTIATE VARIABLES AND SETTINGS FROM YOUR PROVIDER  






## EMAIL SERVICES
EMAIL_HOST = '******'
EMAIL_PORT = '******'
EMAIL_USE_SSL = '******'
EMAIL_HOST_USER = '******'
EMAIL_HOST_PASSWORD = '******'
