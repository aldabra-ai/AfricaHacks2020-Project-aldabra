from django.db import models
from django.conf import settings
from .hospital import Hospital
from django.shortcuts import reverse


class DoctorOffice(models.Model):
    office_owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='doctor_office',on_delete=models.PROTECT, verbose_name='Office Owner')
    office_name = models.CharField(max_length=400)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    first_consultation_fee = models.FloatField()
    follow_up_cons_fee = models.FloatField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10) 

    def __str__(self):
        return self.office_name

    class Meta:
         verbose_name = "Doctor's Office"
         verbose_name_plural = "Doctor Offices"

    def get_absolute_url(self):
        return reverse('hospitaldb:offices-detail', kwargs={
            'office_owner': self.office_owner
            })


class OfficeSchedule(models.Model):

    AVAILABILITY = [
        ('AV', 'Available'),
        ('UA', 'Unavailable')
    ]

    office = models.ForeignKey(DoctorOffice, on_delete=models.CASCADE)
    day_available = models.DateField(unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    availability = models.CharField(max_length=2, choices=AVAILABILITY, default=AVAILABILITY[0])
    reason_for_unavailability = models.CharField(max_length=2000, blank=True)


    def __str__(self):
        return self.office.office_name

    class Meta:
        verbose_name = "Doctor's Schedule"
        verbose_name_plural = 'Doctors Schedule'