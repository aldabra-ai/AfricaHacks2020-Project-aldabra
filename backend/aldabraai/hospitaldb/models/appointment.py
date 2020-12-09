from .doctor import Doctor
from django.db import models
from django.urls import reverse
from patient.models import Patient
from .nurse import Nurse
from .hospital import Hospital


class Appointment(models.Model):
    appointment_id = models.BigIntegerField()
    patient_name = models.CharField(max_length=250)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    prep_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    appointment_for = models.CharField(max_length=450)
    physician = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_dt_time = models.DateTimeField('start date and time')
    end_dt_time = models.DateTimeField('end date and time')
    examination_room = models.CharField(max_length=450)

    def __str__(self):
        return self.appointment_for
