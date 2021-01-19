from django.db import models
from .doctor import Doctor
from django.conf import settings

class DoctorQualification(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    qualification_name = models.CharField('Qualification Name', max_length=700)
    institute_name = models.CharField('Name Of Institution', max_length=700)
    procurement_year = models.DateField('Precurment Date in YYY-MMM-DDD')


    def __str__(self):
        return self.doctor


    class Meta:
        ordering = ['doctor']
        verbose_name = "Doctor's Qualification"
            


