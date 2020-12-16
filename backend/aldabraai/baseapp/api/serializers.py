from django.db.models import fields
from rest_framework import serializers
from .models import StaticAppInfo
from rest_framework import serializers


class StaticinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticAppInfo
        fields = ['company_name', 'app_name', 'webapp_url', 'date_founded']
        
