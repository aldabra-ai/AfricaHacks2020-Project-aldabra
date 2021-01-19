from django.db import models
from django.conf import settings
from hospitaldb.models import Hospital



class Doctor(models.Model):
    full_name = models.CharField('Full Name', max_length=500)
    doctor_id = models.CharField('Doctors ID', max_length=10, unique=True)
    residing_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True)
    practicing_from = models.DateField()
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
        

class AffiliatedHospital(models.Model):
    affiliated_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    hospital_name = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    affiliation_relationship = models.CharField(max_length=500, help_text='What relationship do have with the hospital, what do you do there')
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.affiliated_doctor



