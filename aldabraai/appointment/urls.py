## URL COMMON
from django.urls import (
    path, 
    include
)
## DRF
from rest_framework import routers

## API Views
from .api import (
    # views
    BookAppointmentAPI, 
    BookedAppointmentsAPI,
    RequestedAppointmentsAPI,

    # viewsets
    BaseAppointmentAPI,
    RescheduleAppointmentAPI,
    AddPrepNurseAPI,
    )

## FBVs
from .views import (
    notifyDoctor, 
    acceptSetTimer
    )

app_name = 'appointments'

router = routers.DefaultRouter()
router.register('', BaseAppointmentAPI, basename='appointment')
router.register('reschedule', RescheduleAppointmentAPI, basename='reschedule')
router.register('set/prepnurse', AddPrepNurseAPI, basename='setprepnurse')


urlpatterns = [
    path('book/<office_owner>/', BookAppointmentAPI.as_view(), name='book'),
    path('notify-doctor/<appointment_id>/', notifyDoctor, name='notify_doctor'),
    path('accept-set-timer/<appointment_id>/', acceptSetTimer, name='accept_set_timer'),
    path('booked/', BookedAppointmentsAPI.as_view(), name='booked'),
    path('requested/', RequestedAppointmentsAPI.as_view(), name='requested')
]

urlpatterns += router.urls