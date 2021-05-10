import os
import json
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