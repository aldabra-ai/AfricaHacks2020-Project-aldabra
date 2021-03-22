from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'booked_doctor_office',
        'appointment_date',
        'appointment_for',
        'appointment_date',
        'appointment_time',
        'appointment_end_time',
        'appointment_state',
        'appointment_status',
        'booking_channel',
        'appointment_id'
    ]

    list_filter = [
        'patient',
        'booked_doctor_office',
        'appointment_date',
        'appointment_for',
        'appointment_date',
        'appointment_time',
        'appointment_end_time',
        'appointment_state',
        'appointment_status',
        'booking_channel',
    ]

    list_per_page = 1000

    date_hierarchy = 'appointment_date'

    time_hierarchy = 'appointment_time'

    search_fields = [
        'patient',
        'booked_doctor_office',
        'appointment_date',
        'appointment_for',
        'appointment_date',
        'appointment_time',
        'appointment_end_time',
        'appointment_state',
        'appointment_status',
        'booking_channel',
        'appointment_id'
    ]
