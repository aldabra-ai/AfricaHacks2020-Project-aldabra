## MODELS
from ..models import Patient
## SERIALIZERS
from .patient_serializers import PatientDetailSerializer
## REST FRAMEWORK IMPORTS
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.response import Response
## COMMON
from django.shortcuts import get_object_or_404, redirect

class PatientProfileAPIView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'slug'

    def create(self, *args, **kwargs):
        response = super(PatientProfileAPIView, self).create(*args, **kwargs)
        #return redirect('accounts:set-profile-slug')
        return Response(response)

    def perform_create(self, serializer):
        user = self.request.user
        username = user.identifier
        full_name = user.full_name
        serializer.save(owner=self.request.user, full_name=full_name, slug=username)