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
router.register('patient', PatientProfileAPIView, basename='patient')
router.register('doctor', DoctorProfileAPIView, basename='doctor')
router.register('doctor_specializations', DoctorSpecializationAPI, basename='doctor-specialization')
router.register('doctor_qualifications', DoctorQualificationAPI, basename='doctor-qualification')
router.register('bank_details', PatientBankDetailAPI, basename='bank-details')
router.register('insurrance_detail', PatientIsurranceDetailAPI, basename='insurrance-details')
router.register('reviews', DoctorReviewAPI, basename='review')

urlpatterns = [
    path('set_profile_slug/', setProfileSlug, name='set-profile-slug'),
    path('add/doctor/review/<slug>/', review_doctor, name='review-doctor')
]

urlpatterns += router.urls