from django.db import models
from .hospital import Hospital


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
    position = models.CharField(max_length=500)
    trained_in = models.ManyToManyField(Speciality)
    
    cert_date = models.DateField('Certification Date')
    cert_exp = models.DateField('Certification Expires')
    slug = models.SlugField()

    def __str__(self):
        return self.name