## REST FRAMEWORK IMPORTS
from rest_framework import routers

## COMMON
from django.urls import path

## API CLASSES
from .api import (
    #### Patient's
    PatientProfileAPIView, 
    PatientBankDetailAPI, 
    PatientIsurranceDetailAPI, 
    DoctorReviewAPI,
    review_doctor,

    #### Doctor's
    DoctorProfileAPIView, 
    DoctorQualificationAPI, 
    DoctorSpecializationAPI,

)

## VIEW FUNCTION
from .views import setProfileSlug


app_name = 'accounts'

router = routers.DefaultRouter()
router.register('patients', PatientProfileAPIView, basename='patient')
router.register('doctors', DoctorProfileAPIView, basename='doctor')
router.register('doctor-specializations', DoctorSpecializationAPI, basename='doctor_specialization')
router.register('doctor-qualifications', DoctorQualificationAPI, basename='doctor_qualification')
router.register('bank-details', PatientBankDetailAPI, basename='bank_details')
router.register('insurrance-detail', PatientIsurranceDetailAPI, basename='insurrance_details')
router.register('reviews', DoctorReviewAPI, basename='reviews')

urlpatterns = [
    path('set-profile-slug/', setProfileSlug, name='set-profile-slug'),
    path('doctors/review/<slug>/', review_doctor, name='review_doctor')
]

urlpatterns += router.urls