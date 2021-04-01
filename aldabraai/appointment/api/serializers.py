#### REST FRAMEWORK ####
from rest_framework import serializers

#### MODELS ####
from ..models import Appointment


# class RetrieveAppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = [
#             'patient', 
#             'booked_doctor_office',
#             'appointment_for',
#             'appointment_date',
#             'appointment_time',
#             'appointment_end_time',
#             'short_note',
#             'booking_channel',
#             ]


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    booked_doctor_office = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    appointment_id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Appointment
        fields = [ 
            'id',
            'patient',
            'phone_number',
            'booked_doctor_office',
            'appointment_for',
            'appointment_date',
            'appointment_time',
            'appointment_end_time',
            'short_note',
            'booking_channel',
            'appointment_id',
            ]


            


class DoctorResaonSerializer(serializers.ModelSerializer):
    doctor_rej_reason = serializers.CharField(min_length=20)
    class Meta:
        fields = [
            'doctor_rej_reason'
        ]


class RescheduleAppointmentSerializer(serializers.ModelSerializer):
    appointment_date = serializers.DateField()
    appointment_time = serializers.TimeField()
    
    class Meta:
        model = Appointment
        fields = [
            'appointment_date',
            'appointment_time',
            'prep_nurse'
        ]


class SetPrepNurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'prep_nurse'
        ]

    
class BookedAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment 
        fields = [
            'patient', 
            'booked_doctor_office',
            'appointment_for',
            'appointment_date',
            'appointment_time',
            'appointment_end_time',
            'short_note',
            'booking_channel',
            'appointment_id'
        ]

class RequestedAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'patient', 
            'booked_doctor_office',
            'appointment_for',
            'appointment_date',
            'appointment_time',
            'appointment_end_time',
            'short_note',
            'booking_channel',
            'appointment_id',
        ]