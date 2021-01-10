from ..models import StaticSiteInfo, Feature, Sponsor
from .serializers import SiteInfoSerializer, FeatureSerializer, SponsorSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class StaticSiteInfoViewSet(ReadOnlyModelViewSet):
    """
    Just retrieve only the Sites Static Infos
    """
    queryset = StaticSiteInfo.objects.all()
    serializer_class = SiteInfoSerializer


class FeatureViewSet(ReadOnlyModelViewSet):
    """
    Retrieve all Active Features available
    """
    queryset = Feature.active_features.all()
    serializer_class = FeatureSerializer


class SponsorViewSet(ReadOnlyModelViewSet):
    """
    Retrieve all Sponsors
    """
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

