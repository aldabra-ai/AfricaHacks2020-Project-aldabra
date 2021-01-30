from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.serializers import Serializer
from .serializers import CreateAppointmentSerializer,RetrieveAppointmentSerializer,DoctorResaonSerializer,RescheduleAppointmentSerializer,SetPrepNurseSerializer
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import viewsets
from ..models import Appointment
from django.shortcuts import redirect
from authend.models import User
from django.shortcuts import get_object_or_404
from rest_framework.reverse import reverse
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response



class CreateAppointmentAPI(CreateAPIView):
    model = Appointment
    serializer_class = CreateAppointmentSerializer

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


    # @action(detail=True, methods='post', url_path='reschedule_appointment',name='reschedule-appointment')
    # def reschedule_appointment(self, request, pk):
    #     appointment = self.get_object()
    #     serializer = RescheduleAppointmentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         date = serializer.validated_data['appointment_date']
    #         time = serializer.validated_data['time']
    #         appointment.appointment_date = date
    #         appointment.time = time
    #         appointment.save()
    #         return Response(serializer.data)

        
        


    

        



    