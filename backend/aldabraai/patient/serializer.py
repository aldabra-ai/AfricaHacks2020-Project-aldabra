from django.db.models import fields
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    model = Patient
    fields = [
        'name', 
        'address', 
        'phone', 
        'pcp', 
        'family_phone'
        ]
