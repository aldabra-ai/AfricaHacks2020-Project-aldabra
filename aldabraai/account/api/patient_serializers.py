from rest_framework import serializers
from ..models import Patient



class PatientDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(read_only=True)
    full_name = serializers.ReadOnlyField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id',
            'full_name', 
            'home_address',
            'city',
            'country',
            'phone',
            'family_or_emerg_phone'
        ]