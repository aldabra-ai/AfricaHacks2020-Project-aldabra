from django.db import models
from .doctor import  Doctor
from django.conf import settings


class Specialization(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name



class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)


    def __str__(self):
        return self.doctor

    class Meta:
        ordering = ['doctor']
        verbose_name = "Doctor's Specialization"
        verbose_name_plural = "Doctor's Specialization(s)"
