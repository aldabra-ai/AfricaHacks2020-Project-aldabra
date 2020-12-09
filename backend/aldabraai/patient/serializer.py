from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    pcp = serializers.ReadOnlyField()
    class Meta:
        model = Patient
        fields = [
            'name', 
            'address', 
            'phone', 
            'pcp', 
            'family_phone'
            ]
