from django.db import models
from hospitaldb.models import DoctorOffice,Nurse
from django.conf import settings
from django.shortcuts import reverse 


class BookedAppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(appointment_state='AC')

class RequestedAppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(appointment_state='RE')

class DueAppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(appointment_status='DU')

class TakenAppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(appointment_status='TK')

class OnAppAppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(booking_channel='OP')


class OnCallAppointmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(booking_channel='OC')


class Appointment(models.Model):
    APPOINTMENT_STATE = [
        ('RE', 'Requested'),
        ('AC', 'Accepted'),
        ('DE', 'Declined')
    ]

    APPOINTMENT_STATUS = [
        ('DU', 'Due'),
        ('TK', 'Taken'),
    ]

    BOOKING_CHANNEL = [
        ('OP', 'App'),
        ('OC', 'Call'),
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='patient_appointments',on_delete=models.CASCADE)
    booked_doctor_office = models.ForeignKey(DoctorOffice, related_name='appointments', on_delete=models.CASCADE)
    appointment_for = models.CharField(max_length=500, blank=True)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)
    appointment_end_time = models.TimeField(blank=True, null=True)
    appointment_state = models.CharField(max_length=10, choices=APPOINTMENT_STATE, default=APPOINTMENT_STATE[0][0])
    short_note = models.CharField(max_length=500, blank=True)
    appointment_status = models.CharField(max_length=5, choices=APPOINTMENT_STATUS, default=APPOINTMENT_STATUS[0][0])
    booking_channel = models.CharField(max_length=5, choices=BOOKING_CHANNEL, default=BOOKING_CHANNEL[0][0])
    prep_nurse = models.ForeignKey(Nurse, on_delete=models.PROTECT, blank=True, null=True)
    appointment_id = models.CharField(max_length=7, unique=True, blank=True)
    doctor_dec_reason = models.CharField("Doctor's Reason for Declining Appointment", max_length=450, blank=True)

    ## Managers

    # default
    objects = models.Manager()

    # costum
    booked_appointments = BookedAppointmentManager()
    requested_appointments = RequestedAppointmentManager()
    due_appointments = DueAppointmentManager()
    taken_appointments = TakenAppointmentManager()
    onapp_appointments = OnAppAppointmentManager()
    oncall_appointments = OnCallAppointmentManager()


    def __str__(self):
        return self.appointment_for

    def get_absolute_url(self):
        return reverse('appointment-detail', kwargs={'pk':self.pk})
    class Meta:
        ordering = ['-appointment_date']

    

