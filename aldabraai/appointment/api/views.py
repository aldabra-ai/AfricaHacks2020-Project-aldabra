from aldabraai.appointment.models import appointment
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

    def send_email_notification(self, pk):
        appointment = self.get_object(pk)
        doctor_email = appointment.get_doctor_email

        sender = 'amidbidee@gmail.com'
        appointment_url = appointment.get_absolute_url
        
        subject, from_email, to = "Appointment Request", f'{sender}', f'{doctor_email}'
        text_content = "Someone Requested an Appointment with you, please review it here"
        html_content = f'<p>Someone Requested an Appointment with you, please review it <a href={appointment_url}>here</a></p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()





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

        
        


    

        



    