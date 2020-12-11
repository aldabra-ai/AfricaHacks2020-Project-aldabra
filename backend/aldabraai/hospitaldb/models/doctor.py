from django.db import models
from .hospital import Hospital
from django.urls import reverse


class Speciality(models.Model):
    name = models.CharField(max_length=500)
    treatment = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Specialities'

class Doctor(models.Model):
    doctor_id = models.BigIntegerField()
    name = models.CharField(max_length=250)
    works_in = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    trained_in = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    cert_date = models.DateField(verbose_name='Certification Date')
    cert_exp = models.DateField(verbose_name='Certification Expires')
    #slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('hospitaldb:doctor-bio', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']