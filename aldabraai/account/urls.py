## API CLASS
from .api import PatientProfileAPIView, DoctorProfileAPIView
## REST FRAMEWORK IMPORTS
from rest_framework import routers
## COMMON
from django.urls import path
## VIEW FUNCTION
from .views import setProfileSlug

app_name = 'accounts'

router = routers.DefaultRouter()
router.register('patient', PatientProfileAPIView, basename='patient')
router.register('doctor', DoctorProfileAPIView, basename='doctor')

urlpatterns = [
    path('set_profile_slug/', setProfileSlug, name='set-profile-slug')
]

urlpatterns += router.urls