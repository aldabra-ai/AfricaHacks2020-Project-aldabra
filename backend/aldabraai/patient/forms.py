from django.forms import ModelForm
from .models import Patient

class PatientProfile(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'address', 'phone', 'family_phone']