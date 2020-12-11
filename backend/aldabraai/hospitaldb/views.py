# from rest_framework import status
# from rest_framework.serializers import Serializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.views.generic import DetailView, ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .models import Appointment,Speciality,Doctor,Nurse,Hospital,Room,Block
from django.urls import reverse_lazy
from django.db.models import Q
# from .serializer import HospitalSerializer,AppointmentSerializer,DoctorSerializer,SpecialitySerializer,NurseSerializer,RoomSerializer,BlockSerializer
# from rest_framework import generics

hosp_temp_de = 'hospital/detailviews'
hosp_temp_li = 'hospital/listviews'
hosp_temp_forms = 'hospital/forms'

def auth0dashboard(request, pk):
    pass

class HospitalList(ListView):
    model = Hospital
    template_name = 'hospital/listviews/hospitals.html'

class HospitalDashboard(DetailView):
    model = Hospital
    template_name = 'hospital/dashboards/aldabra-hospital-dashboard.html'
    context_object_name = 'hospital'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class CreateHospitalProfile(CreateView):
    model = Hospital
    fields = ['name', 'address', 'hospital_type',]
    template_name = 'hospital/forms/create_hospital_form.html'
    success_url = reverse_lazy('aldabra-hospital-dashboard')


class DoctorBio(DetailView):
    model = Doctor
    template_name = 'hospital/detailviews/doctor_bio.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class AddDoctor(CreateView):
    model = Doctor
    fields = ['doctor_id', 'name', 'works_in', 'trained_in', 'cert_date', 'cert_exp']
    template_name = 'hospital/forms/add_doctor_form.html'
    success_url = reverse_lazy('doctor-list')

class UpdateDocInfo(UpdateView):
    model = Doctor
    fields = ['doctor_id', 'name', 'works_in', 'trained_in', 'cert_date', 'cert_exp']
    template_name = 'hospital/forms/update_doctor_form.html'
    success_url = reverse_lazy('doctor-bio')

class DoctorList(ListView):
    model = Doctor
    template_name = 'hostpital/list_views/doctors.html'
    context_object_name = 'doctor'


class SearchResultsView(ListView):
    model = Doctor
    template_name = 'hospital/search/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Doctor.objects.filter(
            Q(name__icontains=query) | Q(trained_in__name__icontains=query)
        )
        return object_list



class CreateAppointment(CreateView):
    model = Appointment

    # def get_object(self, pk, queryset):
    #     return super().get_object(queryset=queryset)
    fields = ['patient_name', 'phone', 'emergency_contact', 'appointment_for', 'physician', 'start_dt_time']
    success_url = reverse_lazy('patient-dashboard')
    template_name = 'hospital/forms/create_appointment_form.html'

























# class HospitalList(APIView):
#     """
#     List All Hospitals
#     """
#     def get(self, request, format=None):
#         hospitals = Hospital.objects.all()
#         serializer = HospitalSerializer(hospitals, context={'request': request},many=True)
#         return Response(serializer.data)

#     def post(sefl, request, format=None):
#         serializer = HospitalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HospitalDetail(APIView):
#     """
#     Retrieve, update or delete a hospital instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Hospital.objects.get(pk=pk)
#         except Hospital.DoesNotExist:
#             raise Http404

#     def get(self, rquest, pk, format=None):
#         hospital = self.get_object(pk)
#         serializer = HospitalSerializer(hospital)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         hospital = self.get_object(pk)
#         serializer = HospitalSerializer(hospital, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class DoctorList(APIView):
#     """
#     Retrieve Doctor List
#     """

#     def get(self, request, format=None):
#         doctors = Doctor.objects.all()
#         serializer = DoctorSerializer(doctors, context={'request': request},many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = DoctorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DoctorDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Doctor.objects.get(pk=pk)
#         except Doctor.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         doctor = self.get_object(pk)
#         serializer = DoctorSerializer(doctor)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         doctor = self.get_object(pk)
#         serializer = DoctorSerializer(doctor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class NurseList(generics.ListCreateAPIView):
#     queryset = Nurse.objects.all()
#     serializer_class = NurseSerializer

# class NurseDetail(generics.RetrieveUpdateAPIView):
#     queryset = Nurse.objects.all()
#     serializer_class = NurseSerializer

# class AppointmentList(generics.ListCreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

# class AppointmentDetail(generics.RetrieveDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
    
# class RoomList(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

# class RoomDetail(generics.RetrieveUpdateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# class BlockList(generics.ListCreateAPIView):
#     queryset = Block.objects.all()
#     serializer_class = RoomSerializer

# class BlockDetail(generics.RetrieveUpdateAPIView):
#     queryset = Block.objects.all()
#     serializer_class = BlockSerializer


