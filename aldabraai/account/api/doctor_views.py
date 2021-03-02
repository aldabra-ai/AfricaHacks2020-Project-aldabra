## MODELS
from ..models import Doctor, DoctorQualification,DoctorSpecialization
## SERIALIZERS
from .doctor_serializers import DoctorDetailSerializer, DoctorQualificationSerializer,DoctorSpecializationSerializer
## REST FRAMEWORK IMPORTS
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
## COMMON
from django.shortcuts import get_object_or_404, redirect


class CreateUpdateRetrieveViewset(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  viewsets.GenericViewSet):
        pass


class DoctorProfileAPIView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'slug'

    def create(self, *args, **kwargs):
        response = super(DoctorProfileAPIView, self).create(*args, **kwargs)
        #return redirect('accounts:set-profile-slug')
        return Response(response.data)

    def perform_create(self, serializer):
        user = self.request.user
        username = user.identifier
        full_name = user.full_name
        serializer.save(owner=user, full_name=full_name, slug=username)



class DoctorQualificationAPI(CreateUpdateRetrieveViewset):
    queryset = DoctorQualification.objects.all()
    serializer_class = DoctorQualificationSerializer
    lookup_field = 'pk'

    def get(self, pk):
        return get_object_or_404(DoctorQualification, pk=pk)

    def create(self, request, *args, **kwargs):
        response = super(DoctorQualificationAPI, self).create(request, *args, **kwargs)

        return Response(response.data)

    def update(self, request, *args, **kwargs):
        response = super(DoctorQualificationAPI, self).update(request, *args, **kwargs)

        return Response(response.data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(doctor=user)


class DoctorSpecializationAPI(CreateUpdateRetrieveViewset):
    queryset = DoctorSpecialization.objects.all()
    serializer_class = DoctorSpecializationSerializer
    lookup_field = 'pk'        

    def get(self, pk):
        return get_object_or_404(DoctorSpecialization, pk=pk)

    def create(self, request, *args, **kwargs):
        response = super(DoctorSpecializationAPI, self).create(request, *args, **kwargs)

        return Response(response.data)


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(doctor=user)

