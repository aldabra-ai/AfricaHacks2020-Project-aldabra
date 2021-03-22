from .viewsets import (
    PatientProfileAPIView, 
    PatientBankDetailAPI, 
    PatientIsurranceDetailAPI, 
    DoctorReviewAPI, 
    #review_doctor,

    #### Doctor viewsets ####
    DoctorProfileAPIView, 
    DoctorQualificationAPI, 
    DoctorSpecializationAPI
)

from .views import review_doctor
