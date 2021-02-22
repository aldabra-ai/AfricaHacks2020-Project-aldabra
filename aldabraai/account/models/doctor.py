from django.db import models
from django.conf import settings
from hospitaldb.models import Hospital
from django.shortcuts import reverse


class Doctor(models.Model):
    full_name = models.CharField(max_length=300, blank=True)
    doctor_id = models.CharField('Doctors ID', max_length=10, unique=True)
    residing_hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    practicing_from = models.DateField()
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='doctor_profile', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.full_name

    @property
    def doctor_full_name(self):
        return self.owner.full_name

    def get_absolute_url(self):
        return reverse('accounts:doctor-profile-detail', kwargs={
                                                        'slug': self.slug}
            )
    class Meta:
        ordering = ['residing_hospital']
        

class AffiliatedHospital(models.Model):
    affiliated_doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='affiliated_hospitals', on_delete=models.CASCADE) 
    hospital_name = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    affiliation_relationship = models.CharField(max_length=500, help_text='What relationship do have with the hospital, what do you or did you do there?')
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.affiliated_doctor


