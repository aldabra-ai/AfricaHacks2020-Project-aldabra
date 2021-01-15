from django.db import models
from django.urls import reverse
from django.conf import settings
from hospitaldb.models import Hospital


class MedicalRecord(models.Model):

    CHICKEN_POX_IMMUN = [
        ('IMM', 'IMMUNE'),
        ('NIM', 'NOT IMMUNE')
    ]

    MEASLES_IMMUN = [
        ('IMM', 'IMMUNE'),
        ('NIM', 'NOT IMMUNE')
    ]

    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    birth_date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    em_cont_name = models.CharField('Emergency Contact Name', max_length=150)
    em_cont_hm_ph = models.CharField('Emergency Conatact Home Phone', max_length=20)
    em_cont_add = models.CharField('Emergency Contact Address', max_length=250)
    em_cont_wrk_ph = models.CharField('Emergency Contact Work Phone',max_length=250)
    chicken_pox = models.CharField(max_length=20, choices=CHICKEN_POX_IMMUN)
    measles = models.CharField(max_length=20, choices=MEASLES_IMMUN)
    had_hep_b = models.BooleanField('Had Hapatitis B?')
    medical_p_list = models.TextField('Medical Problems')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(Hospital)

    def __str__(self):
        self.first_name
