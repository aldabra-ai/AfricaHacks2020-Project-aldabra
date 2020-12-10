from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Patient
from hospitaldb.models import Doctor
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    pa

class PatientSerializer(serializers.ModelSerializer):
    pcp = serializers.PrimaryKeyRelatedField(many=True, queryset=Doctor.objects.all())
    class Meta:
        model = Patient
        fields = [
            'name', 
            'address', 
            'phone', 
            'pcp', 
            'family_phone'
            ]

