from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import  APITestCase
from .models import Appointment

class AppointmentTests(APITestCase):
    def check_get_appointment(self):
        """
        Ensure we can get an appointment
        """
        client = self.client
        client.force_authentication(user=None, token=None)

        url = reverse('appointment:base-appointment-detail')
        data = Appointment.objects.get(appointment_id='appt57')
        response = client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # def test_create_appointment(self):
    #     """
    #     Ensure we can create a new appointment
    #     """
    #     client = self.client
    #     client.force_authenticate(user=None, token=None)


    #     url = reverse('appointment:base-appointment-list')
    #     data = {
    #         'booked_doctor_office':  5,
    #         'appointment_for': 'Migrain',
    #         'appointment_date': '2021-02-21',
    #         'appointment_time': '11:45:30',
    #         'short_note': '',
    #         'booking_channel': 'OP',
    #     }

    #     response = client.post(url, data)

    #     ## make sure this returns an 201 status code else raise an error
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


