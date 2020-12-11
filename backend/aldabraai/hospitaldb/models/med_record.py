from django.db import models
from django.urls import reverse

from django.conf import settings


class MedicalRecords(models.Model):

    CHICKEN_POX_IMMUN = [
        ('IMM', 'IMMUNE'),
        ('NIM', 'NOT IMMUNE')
    ]

    MEASLES_IMMUN = [
        ('IMM', 'IMMUNE'),
        ('NIM', 'NOT IMMUNE')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    birth_date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    em_cont_name = models.CharField(max_length=150)
    em_cont_hm_ph = models.CharField(max_length=20)
    em_cont_add = models.CharField(max_length=250)
    em_cont_wrk_ph = models.CharField(max_length=250)
    chicken_pox = models.CharField(max_length=20, choices=CHICKEN_POX_IMMUN)
    measles = models.CharField(max_length=20, choices=MEASLES_IMMUN)
    had_hep_b = models.BooleanField()
    medical_p_list = models.TextField()
