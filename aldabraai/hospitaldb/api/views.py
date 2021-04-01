from rest_framework.generics import mixins
from rest_framework.decorators import action

from ..models import DoctorOffice

from .serializers import (
    DoctorOfficeSerializer,
    OfficeScheduleSerializer
)

from django.shortcuts import get_object_or_404

