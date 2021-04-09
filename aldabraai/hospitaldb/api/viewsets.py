## DRF imports
import re
from rest_framework.generics import mixins
from rest_framework import (
    viewsets,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

## MODELS 
from ..models import (
    #Hospital,
    DoctorOffice,
    OfficeSchedule,
    #MedicalRecord,
    #Room,
    #Block,
    #Department,
)

from authend.models import User

## SERIALIZERS
from .serializers import (
    DoctorOfficeSerializer,
    OfficeScheduleSerializer
)

## COMMON
from django.shortcuts import get_object_or_404




class DoctorOfficeAPI(viewsets.ModelViewSet):
    queryset = DoctorOffice.objects.all()
    serializer_class = DoctorOfficeSerializer
    lookup_field = 'office_owner'

    def create(self, request, *args, **kwargs):
        response = super(self, DoctorOfficeAPI).create(request, *args, **kwargs)

        return Response(response.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        user = self.request.user
        office = DoctorOffice.objects.get(office_owner=user)

        # check if office already exists
        if office.exist():
            return Response('You can only get one office')
        else:
            return serializer.save(office_owner=user)

    def get_object(self):
        office_owner = User.objects.get(identifier=self.kwargs['office_owner'])
        return get_object_or_404(DoctorOffice, office_owner=office_owner)


    @action(detail=True, methods=['GET'], url_name='office-schedules', url_path='schedules')
    def officeSchedules(self, request, office_owner, pk=None):
        office = self.get_object()
        serializer = self.serializer_class = OfficeScheduleSerializer

        queryset = OfficeSchedule.objects.filter(office=office)
        serializer = OfficeScheduleSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], url_name='add_schedule', url_path='add-schedule')
    def addSchedule(self, request, office_owner):
        office = self.get_object()
        serializer = OfficeScheduleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(office=office)

        return Response(serializer.data, status=status.HTTP_200_OK)

class DoctorOfficeScheduleAPI(viewsets.ModelViewSet):
    serializer_class = OfficeScheduleSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        office = user.doctor_office
        return OfficeSchedule.objects.filter(office=office)

    # def get_object(self, pk=None):
    #     return get_object_or_404(queryset, pk=pk)

    def create(self, request, *args, **kwargs):
        response = super(self, DoctorOfficeAPI).create(request, *args, **kwargs)

        return Response(response.data, status=status.HTTP_200_OK)
