from django.db import models
from django.conf import settings
from hospitaldb.models import Hospital

class Doctor(models.Model):
    full_name = models.CharField('Full Name', max_length=500)
    doctor_id = models.CharField('Doctors ID', max_length=10, unique=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    speciality = models.CharField('Speciality or Specialities')
    is_verified = models.BooleanField(default=False)
    is_certified = models.BooleanField(default=False)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
        


