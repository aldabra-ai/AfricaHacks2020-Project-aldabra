from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import HospitalList, HospitalDetail, DoctorList, DoctorDetail,NurseList,NurseDetail,BlockList,BlockDetail,RoomList,RoomDetail,AppointmentList,AppointmentDetail
from .views import HospitalDashboard, CreateHospitalProfile,AddDoctor,UpdateDocInfo,DoctorBio, DoctorList, SearchResultsView,CreateAppointment

app_name = 'hospitaldb'

# urlpatterns = [
#     path('hospital/<int:pk>/dashboard/', HospitalDetail.as_view(), name='hospital'),
#     path('doctors/', DoctorList.as_view()),
#     path('doctor/<int:pk>/', DoctorDetail.as_view(), name='doctor'),
#     path('nurses/', NurseList.as_view()),
#     path('nurse/<int:pk>/', NurseDetail.as_view()),
#     path('appointments/', AppointmentList.as_view()),
#     path('appointment/<int:pk>/', AppointmentDetail.as_view()),
#     path('rooms/', RoomList.as_view()),
#     path('room/<int:pk>/', RoomDetail.as_view()),

# ]

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('create-profile/', CreateHospitalProfile.as_view(), name='create-hospital'),
    path('aldabra-dashboard/<int:pk>', HospitalDashboard.as_view(),  name='aldabra-hospital-dashboard'),
    path('doctor/bio/<int:pk>/', DoctorBio.as_view(), name='doctor-bio'),
    path('doctor/add/', AddDoctor.as_view(), name='add-doctor'),
    path('doctor/<int:pk>/update', UpdateDocInfo.as_view(), name='update-doc-info'),
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('appointment/create/', CreateAppointment.as_view(), name='create-appointment')
]

#urlpatterns = format_suffix_patterns(urlpatterns)
