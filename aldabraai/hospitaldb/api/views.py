from rest_framework.generics import mixins
from rest_framework import viewsets
from ..models import DoctorOffice
from appointment.models import Appointment
from appointment.api import AppointmentSerializer
from .serializers import DoctorOfficeSerializer,OfficeScheduleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class DoctorOfficeAPI(viewsets.ModelViewSet):
    queryset = DoctorOffice.objects.all()
    serializer_class = DoctorOfficeSerializer


    @action(detail=True, methods=['post','get'], url_path='book-appointment')
    def book_appointment(self,request, pk=None):
        doctor_office = get_object_or_404(DoctorOffice, pk=pk)
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(booked_doctor_office=doctor_office, patient=self.request.user)
