## URL COMMON
from django.urls import (
    path, 
    include
)
## DRF
from rest_framework import routers

## API Views
from .api.views import (
    #BaseAppointmentAPI,
    RescheduleAppointmentAPI,
    AddPrepNurseAPI, 
    BookedAppointmentsAPI,
    RequestedAppointmentsAPI
    )

## FBVs
from .views import notifyDoctor, acceptSetTimer

app_name = 'appointments'

router = routers.DefaultRouter()
#router.register('', BaseAppointmentAPI, basename='base-appointment')
router.register('reschedule', RescheduleAppointmentAPI, basename='reschedule')
router.register('set/prepnurse', AddPrepNurseAPI, basename='setprepnurse')


urlpatterns = [
    path('notify-doctor/<pk>/', notifyDoctor, name='notify_doctor'),
    path('accept-set-timer/<pk>/', acceptSetTimer, name='accept_set_timer'),
    path('booked/', BookedAppointmentsAPI.as_view(), name='booked'),
    path('requested/', RequestedAppointmentsAPI.as_view(), name='requested')
]

urlpatterns += router.urls