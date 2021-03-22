## URL Required Imports
from django.urls import path, include
from rest_framework import routers

## API Views
from .api.views import BaseAppointmentAPI,RescheduleAppointmentAPI,AddPrepNurseAPI, BookedAppointmentsAPI,RequestedAppointmentsAPI

# ## Normal Views
from .views import notifyDoctor, acceptSetTimer

app_name = 'appointment'

router = routers.DefaultRouter()
router.register('', BaseAppointmentAPI, basename='base-appointment')
router.register('reschedule', RescheduleAppointmentAPI, basename='reschedule')
router.register('set_prepnurse', AddPrepNurseAPI, basename='set-prepnurse')

urlpatterns = [
    path('notify_doctor/<pk>/', notifyDoctor, name='notify-doctor'),
    path('accept_set_timer/<pk>/', acceptSetTimer, name='accept-set-timer'),
    path('booked_appointments/', BookedAppointmentsAPI.as_view(), name='booked-appointments'),
    path('requested_appointments/', RequestedAppointmentsAPI.as_view(), name='requested-appointments')
]

urlpatterns += router.urls