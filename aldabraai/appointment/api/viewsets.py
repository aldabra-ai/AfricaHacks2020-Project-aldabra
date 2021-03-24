#### REST FRAMEWORK ####
from rest_framework.generics import (
    mixins, 
    #ListAPIView
    )
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
    #RetrieveAppointmentSerializer,
    DoctorResaonSerializer,
    RescheduleAppointmentSerializer,
    SetPrepNurseSerializer,
    #BookedAppointmentSerializer,
    #RequestedAppointmentSerializer
)

#### MODELS ####
from ..models import Appointment



class UpdateViewsets(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass



class LIstReadUpdateViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass




class BaseAppointmentAPI(LIstReadUpdateViewset):
     queryset = Appointment.objects.all()
     serializer_class = AppointmentSerializer
     lookup_field = 'appointment_id'



class RescheduleAppointmentAPI(UpdateViewsets):
    queryset = Appointment.objects.all()
    serializer_class = RescheduleAppointmentSerializer
    lookup_field = 'appointment_id'

    def update(self, request , appointment_id=None, *args, **kwargs):
        response = super(RescheduleAppointmentAPI, self).update(request, *args, **kwargs)

        appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
        url = appointment.get_accept_set_timer_url()
        return redirect(url)

    def perform_update(self, serializer):
        return serializer.save()



class AddPrepNurseAPI(UpdateViewsets):
    queryset = Appointment.objects.all()
    serializer_class = SetPrepNurseSerializer
    lookup_field = 'appointment_id'

    def update(self, request, appointment_id=None,*args, **kwargs):
        response = super(AddPrepNurseAPI, self).update(request, *args, **kwargs)

        appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
        url = appointment.get_accept_set_timer_url()
        return redirect(url)

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
