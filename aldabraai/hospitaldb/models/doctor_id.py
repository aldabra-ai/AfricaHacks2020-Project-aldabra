from django.db import models
from . import Hospital



class DoctorID(models.Model):
    doctor_id = models.CharField('ID', max_length=10)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_id

    class Meta:
        ordering = ['hospital']
        verbose_name = 'Doctor Hospital ID'
        verbose_name_plural = "Doctor Hospital IDs"