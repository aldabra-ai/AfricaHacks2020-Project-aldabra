## URL Required Imports
from django.urls import path, include
from rest_framework import routers

## API Views
from .api.views import BaseAppointmentAPI

# ## Normal Views
from .views import notify_doctor

app_name = 'appointment'

router = routers.DefaultRouter()
router.register('', BaseAppointmentAPI, basename='create-appointment')

urlpatterns = [
    path('notify_doctor/<pk>/', notify_doctor, name='notify-doctor')
]

urlpatterns += router.urls