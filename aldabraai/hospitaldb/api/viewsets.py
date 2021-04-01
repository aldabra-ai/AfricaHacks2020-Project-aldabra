## DRF imports
from rest_framework.generics import mixins
from rest_framework import viewsets
from rest_framework.decorators import action

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
    DoctorOfficeSerializer,
    OfficeScheduleSerializer
)

## COMMON
from django.shortcuts import get_object_or_404




class DoctorOfficeAPI(viewsets.ModelViewsets):
    


