from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HospitalList, HospitalDetail, DoctorList, DoctorDetail,NurseList,NurseDetail,BlockList,BlockDetail,RoomList,RoomDetail,AppointmentList,AppointmentDetail

app_name = 'hospitaldb'

urlpatterns = [
    path('hospitals/', HospitalList.as_view()),
    path('hospital/<int:pk>/', HospitalDetail.as_view(), name='hospital'),
    path('doctors/', DoctorList.as_view()),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name='doctor'),
    path('nurses/', NurseList.as_view()),
    path('nurse/<int:pk>/', NurseDetail.as_view()),
    path('appointments/', AppointmentList.as_view()),
    path('appointment/<int:pk>/', AppointmentDetail.as_view()),
    path('rooms/', RoomList.as_view()),
    path('room/<int:pk>/', RoomDetail.as_view()),
    path('blocks/', BlockList.as_view()),
    path('block/<int:pk>/', BlockDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
