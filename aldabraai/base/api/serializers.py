from rest_framework import serializers
from ..models import StaticSiteInfo, Feature, Sponsor


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticSiteInfo
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = [
            'name',
            'summary',
            'state',
            ]

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'name',
            'logo',
            'website_url',
        ]