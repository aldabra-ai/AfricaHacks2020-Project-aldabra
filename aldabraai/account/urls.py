## REST FRAMEWORK IMPORTS
from rest_framework import routers

## COMMON
from django.urls import (
    path, 
    include
    )

## API CLASSES
from .api import (
    #### Patient's
    PatientProfileAPIView, 
    PatientBankDetailAPI, 
    PatientIsurranceDetailAPI, 
    DoctorReviewAPI,
    ReviewDoctorAPI,

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
router.register('bank-details', PatientBankDetailAPI, basename='bank_details')
router.register('insurrance-detail', PatientIsurranceDetailAPI, basename='insurrance_details')
router.register('reviews', DoctorReviewAPI, basename='reviews')
router.register('doctors', DoctorProfileAPIView, basename='doctor')
router.register('doctors/doctor-specializations', DoctorSpecializationAPI, basename='doctor_specialization')
router.register('doctors/doctor-qualifications', DoctorQualificationAPI, basename='doctor_qualification')


urlpatterns = [
    path('doctors/review/<slug>/', ReviewDoctorAPI.as_view(), name='review_doctor'),
    path('set-profile-slug/', setProfileSlug, name='set-profile-slug'),
]

urlpatterns += router.urls