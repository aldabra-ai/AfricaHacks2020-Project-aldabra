## API CLASSES
# Doctor's
from .api import DoctorProfileAPIView, DoctorQualificationAPI, DoctorSpecializationAPI
# Patient's
from .api import PatientProfileAPIView, PatientBankDetailAPI, PatientIsurranceDetailAPI, PatientReviewAPI
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
router.register('doctor_specializations', DoctorSpecializationAPI, basename='doctor-specialization')
router.register('doctor_qualifications', DoctorQualificationAPI, basename='doctor-qualification')
router.register('bank_details', PatientBankDetailAPI, basename='bank-details')
router.register('insurrance_detail', PatientIsurranceDetailAPI, basename='insurrance-details')
router.register('review', PatientReviewAPI, basename='review')

urlpatterns = [
    path('set_profile_slug/', setProfileSlug, name='set-profile-slug')
]

urlpatterns += router.urls