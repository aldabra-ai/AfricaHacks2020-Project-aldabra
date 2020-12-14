# from rest_framework import status
# from .serializer import PatientSerializer
# from rest_framework import generics
# from rest_framework.serializers import Serializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404, get_list_or_404,redirect,render
from django.urls import reverse_lazy
from django.http import Http404
from .models import Patient
from .forms import PatientProfile
from django.contrib import messages

#def patientdashboard():
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

@login_required
def edit_profile(request):
    if request.method == 'POST':
        patient_form = PatientProfile(
            instance=request.user.patient,
            data=request.POST)

        if patient_form.is_valid():
            patient_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Error updating your profile')
    
    else:
        patient_form = PatientProfile(instance=request.user.patient)
    
    return render(request, 
                  'patient/forms/create_patient_form.html',
                  {'patient_form': patient_form})


# class UpdatePatientProfile(UpdateView):
#     model = Patient
#     fields = ['name', 'address', 'phone', 'family_phone']
#     template_name = 'patient/forms/update_patient_form.html'
#     success_url = reverse_lazy('patient-dashboard')

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

    
