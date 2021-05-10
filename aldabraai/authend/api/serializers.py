# user model
from django.db import models
from typing_extensions import Required
from ..models import User

# rest framework serializer class
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    pass

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =  [
            'email',
            'username'
        ]