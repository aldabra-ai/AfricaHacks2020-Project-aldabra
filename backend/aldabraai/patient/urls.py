from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PatientList, PatientDetail,edit_profile #CreatePatientProfile, UpdatePatientProfile

urlpatterns = [
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('<int:pk>/', PatientDetail.as_view(), name='patient-dashboard'),
    #path('create_patient_profile/', CreatePatientProfile.as_view(), name='create-patient'),
    #path('update_patient_profile/<int:pk>/', UpdatePatientProfile.as_view(), name='update-patient'),
]