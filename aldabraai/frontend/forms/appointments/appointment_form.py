from django.forms import fields
# appointment model
from appointment.models import Appointment

# form queryset models
from authend.models import User
from hospitaldb.models import DoctorOffice

# common
from django import forms


class AppointmentCreationForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=User.objects.all, widget=forms.HiddenInput)
    booked_doctor_office = forms.ModelChoiceField(queryset=)

    class Meta:
        model = Appointment
        fields = [
            ''
        ]