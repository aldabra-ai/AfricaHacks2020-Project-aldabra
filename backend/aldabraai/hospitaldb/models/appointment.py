from .doctor import Doctor
from django.db import models
from django.urls import reverse
#from patient.models import Patient
from .nurse import Nurse
from .hospital import Hospital
#from django.contrib.auth import  User

class Appointment(models.Model):
    #user = models.ForeignKey('User', related_name='appointments', on_delete=models.CASCADE)
    #appointment_id = models.BigIntegerField()
    patient_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15, blank=True)
    emergency_contact = models.CharField(max_length=15)
    appointment_for = models.CharField(max_length=450)
    physician = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_dt_time = models.DateTimeField('start date and time')
    # end_dt_time = models.DateTimeField('end date and time', blank=True)
    # examination_room = models.CharField(max_length=450, blank=True)
    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment_for

    def get_absolute_url(self):
        return reverse('appointment-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['start_dt_time']

