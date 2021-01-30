## URL Required Imports
from django.urls import path, include
from rest_framework import routers

## API Views
from .api.views import CreateAppointmentAPI

## Normal Views
from .views import notify_doctor





urlpatterns = [
    # CREATE APPOINTMENT API ENDPOINT
    path('create_appointment', CreateAppointmentAPI.as_view(), name='create-appointment'), 
    path('notify-doctor-on-appointment-creation', notify_doctor, name='notify-doctor'),
]
