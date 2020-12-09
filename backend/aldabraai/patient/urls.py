from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PatientList, PatientDetail

urlpatterns = [
    path('patients/', PatientList.as_view()),
    path('patient/<int:pk>/', PatientDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)