# User model
from .models import User

# AuthToken Library
from knox.auth import AuthToken

# timezone
from django.utils import timezone

def GetToken(user):
    token = AuthToken.objects.get(user=user)
    return token.digest

def check_expiry(token):
    token = AuthToken.objects.get(digest=token)
    if token.expiry <= timezone.now():
        token.delete()
        return True
    else:
        return False

 