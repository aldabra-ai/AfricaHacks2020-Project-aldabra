"""
 LOCAL SETTINGS FILE FOR ALDABRA.AI
 WARNING: THIS SHOULD NOT BE USED IN PRODUCTION MODELS
 WARNING: ONLY USE IN DEVELOPMENT

 TO DISABLE THIS SETTINGS: SET 'live=True' IN './__init__' file
"""

from .base import *

DEBUG = True

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = [
    #'0.0.0.0', 
    '127.0.0.1',
    'localhost',
    'aldabraai',
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

        'NAME': get_variable_or_secrete('DB_NAME', limit_to_secret=True),

        'USER': get_variable_or_secrete('DB_USER', limit_to_secret=True),

        'PASSWORD': get_variable_or_secrete('DB_PASSWORD', limit_to_secret=True),

        'HOST': get_variable_or_secrete('DB_HOST', limit_to_secret=True),

        'PORT': get_variable_or_secrete('DB_PORT', limit_to_secret=True),
    }

}

SHARE_URL = "http://127.0.0.1:8000"

# Static assets
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static', 'static_dirs'),
# )
# User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')



## EMAIL SERVICES
SERVER_EMAIL = 'amidbidee@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False 
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = get_variable_or_secrete('EMAIL_PASSWORD', limit_to_secret=True)
EMAIL_HOST_USER = SERVER_EMAIL 
EMAIL_PORT = 587 
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
 


