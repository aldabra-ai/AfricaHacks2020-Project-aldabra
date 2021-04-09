## DRF imports
from rest_framework.generics import (
    mixins
    )
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

## SERIALIZERS
from .serializers import (
    #DoctorOfficeSerializer,
    OfficeScheduleSerializer
)

## COMMON
from django.shortcuts import get_object_or_404



# class CreateReadUpdateDestroyView(
#     mixins.CreateModelMixin, 
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin):
#     pass


# class DoctorOfficeScheduleAPI(CreateReadUpdateDestroyView):
#     serializer_class = OfficeScheduleSerializer
#     lookup_field = 'office'

#     def create(self, request, *args, **kwargs):
#         response = super(self, DoctorOfficeScheduleAPI).create(request, *args, **kwargs)

#         return Response(response.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         return self.create()

#     def perform_create(self, serializer):
#         pass