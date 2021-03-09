#### REST FRAMEWORK ####
from rest_framework.generics import mixins, ListAPIView
from rest_framework import (
    viewsets, 
    #permissions
)
from rest_framework.response import Response
from rest_framework.decorators import action

#### COMMON ####
from django.shortcuts import (
    redirect,
    get_object_or_404
)


#### SERIALIZERS ####
from .serializers import (
    AppointmentSerializer, 
    AppointmentSerializer,
    #RetrieveAppointmentSerializer,
    DoctorResaonSerializer,
    RescheduleAppointmentSerializer,
    SetPrepNurseSerializer,
    BookedAppointmentSerializer,
    RequestedAppointmentSerializer
)

#### MODELS ####
from ..models import Appointment




class CreateAppointmentClass(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass

class UpdateViewsets(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass

class ListViewsets(ListAPIView):
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
        return redirect(redirect_to=f'{url}')

        
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


class BookedAppointmentsAPI(ListViewsets):
    queryset = Appointment.booked_appointments.all()
    serializer_class = BookedAppointmentSerializer

class RequestedAppointmentsAPI(ListViewsets):
    queryset = Appointment.requested_appointments.all()
    serializer_class = RequestedAppointmentSerializer

class RescheduleAppointmentAPI(UpdateViewsets):
    queryset = Appointment.objects.all()
    serializer_class = RescheduleAppointmentSerializer

    def update(self, request , pk=None, *args, **kwargs):
        response = super(RescheduleAppointmentAPI, self).update(request, *args, **kwargs)

        appointment = get_object_or_404(Appointment, pk=pk)
        url = appointment.get_accept_set_timer_url()
        return redirect(redirect_to=f'{url}')

    def perform_update(self, serializer):
        return serializer.save()


class AddPrepNurseAPI(UpdateViewsets):
    queryset = Appointment.objects.all()
    serializer_class = SetPrepNurseSerializer

    def update(self, request, pk=None,*args, **kwargs):
        response = super(AddPrepNurseAPI, self).update(request, *args, **kwargs)

        appointment = get_object_or_404(Appointment, pk=pk)
        url = appointment.get_accept_set_timer_url()
        return redirect(redirect_to=f'{url}')

    def perform_update(self, serializer):
        return serializer.save()

        
        
class AppointmentDeclineReasonAPI(UpdateViewsets):
    queryset = Appointment.objects.all()
    serializer_class = DoctorResaonSerializer

    def update(self, request, pk=None, *args, **kwargs):
        response = super(AppointmentDeclineReasonAPI, self).update(request, *args, **kwargs)

        appointment = get_object_or_404(Appointment, pk=pk)
        url = appointment.get_decline_delete_url()
        return redirect(redirect_to=f'{url}')

    def perform_update(self, serializer):
        return serializer.save()

    

        



    