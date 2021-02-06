from rest_framework import response
from rest_framework.serializers import Serializer
from .serializers import AppointmentSerializer, AppointmentSerializer,RetrieveAppointmentSerializer,DoctorResaonSerializer,RescheduleAppointmentSerializer,SetPrepNurseSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import viewsets, permissions
from rest_framework.generics import mixins
from ..models import Appointment
from django.shortcuts import redirect
from authend.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponseRedirect


class CreateAppointmentClass(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass

class BaseAppointmentAPI(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        response = super(BaseAppointmentAPI, self).create(request, *args, **kwargs)
        
        ## RETRIEVE APPOINTMENT ID AND GET CURRENTLY SAVED APPOINTMENT
        pk = response.data['id']
        appointment = get_object_or_404(Appointment, id=pk)

        ###### THIS WILL BE CHANGED LATER BUT FOR NOW ########
        appointment_id = f"appt_{+pk}"
        appointment.appointment_id = appointment_id
        appointment.save()
        ######      CHANGE IMMINENT     ######################
        
        ## REDIRECT TO NOTIFY DOCTOR FUNCTION
        url = appointment.get_notify_doctor_url()
        return HttpResponseRedirect(redirect_to=f'{url}')

        
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)





        
        


    

        



    