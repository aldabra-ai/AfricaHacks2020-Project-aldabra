# from rest_framework import status
# from .serializer import PatientSerializer
# from rest_framework import generics
# from rest_framework.serializers import Serializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404, get_list_or_404,redirect
from django.urls import reverse_lazy
from django.http import Http404
from .models import Patient

#def patientdashboard():
def patientdashboard(request, pk):
    pass

class PatientList(ListView):
    model = Patient
    template_name = 'patient/list_views/patient_list.html'
    context_object_name = 'patient'

    #def get_context_data(self, **kwargs)
        #return super().get_context_data(**kwargs)

class PatientDetail(DetailView):
    model = Patient
    template_name = 'patient/detail_views/patient.html'
    context_object_name = 'patient'

    #def get_context_data(self, **kwargs)
        #return super().get_context_data(**kwargs)

class CreatePatientProfile(CreateView):
    model = Patient
    fields = ['name', 'address', 'phone', 'family_phone']
    template_name = 'patient/forms/create_patient_form.html'
    success_url = reverse_lazy('patient-list')

class UpdatePatientProfile(UpdateView):
    model = Patient
    fields = ['name', 'address', 'phone', 'family_phone']
    template_name = 'patient/forms/update_patient_form.html'
    success_url = reverse_lazy('patient-dashboard')

class DeletePatientProfile(DeleteView):
    model = Patient
    template_name = 'patient/forms/delete_patient_form.html'
    success_url = reverse_lazy('patient-dashboard')


# class PatientList(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

# class PatientDetail(generics.RetrieveUpdateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

    
