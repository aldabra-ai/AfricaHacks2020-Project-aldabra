#### REST FRAMEWORK ####

from rest_framework.generics import (
    #mixins, 
    ListAPIView,
    CreateAPIView,
    )
from rest_framework import (
    #viewsets, 
    permissions,
    #status
)
from rest_framework.response import Response
#from rest_framework.decorators import action

#### COMMON ####
from django.shortcuts import (
    redirect,
    #get_object_or_404
)
from rest_framework.serializers import Serializer
#rom rest_framework.views import APIView

## utils
from ..utils import (
    #generate_random_string,
    generate_uuid,
)



#### SERIALIZERS ####
from .serializers import (
    AppointmentSerializer, 
    AppointmentSerializer,
    #RetrieveAppointmentSerializer,
    #DoctorResaonSerializer,
    #RescheduleAppointmentSerializer,
    #SetPrepNurseSerializer,
    BookedAppointmentSerializer,
    RequestedAppointmentSerializer
)

#### MODELS ####
from ..models import Appointment
from hospitaldb.models import DoctorOffice
from authend.models import User




class ListView(ListAPIView):
    pass


class BookAppointmentAPI(CreateAPIView):
    '''
    '''

    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        pk = response.data['id']
        appointment = Appointment.objects.get(id=pk)
        url = appointment.get_notify_doctor_url()

        return redirect(url)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

    def perform_create(self, serializer):
        doctor = User.objects.get(identifier=self.kwargs['office_owner'])
        doctor_office = doctor.doctor_office
        appointment_id = generate_uuid(
            use_host=True, 
            use_id=True, 
            use_time=True, 
            rand=False
            )
        serializer.save(
            patient=self.request.user, 
            booked_doctor_office=doctor_office, 
            appointment_id=appointment_id
            )



class BookedAppointmentsAPI(ListView):
    '''
    '''

    queryset = Appointment.booked_appointments.all()
    serializer_class = BookedAppointmentSerializer

class RequestedAppointmentsAPI(ListView):
    '''
    '''

    queryset = Appointment.requested_appointments.all()
    serializer_class = RequestedAppointmentSerializer




    



