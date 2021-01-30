from rest_framework import serializers
from ..models import Appointment
from authend.models import User


class AppointmentSerializer(serializers.ModelSerializer):
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
            'prep_nurse',
            'booking_channel',
            ]



class RetrieveAppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()
    booked_doctor_office = serializers.StringRelatedField()
    appointment_date = serializers.DateField(read_only=True)
    appointment_time = serializers.TimeField(read_only=True)
    appointment_end_time = serializers.TimeField(read_only=True)
    short_note = serializers.ReadOnlyField()
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
            ]


class CreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [ 
            'booked_doctor_office',
            'appointment_for',
            'appointment_date',
            'appointment_time',
            'appointment_end_time',
            'short_note',
            'booking_channel',
            'appointment_id',
            ]


    def get_appointment_id(self):
        appointment_id = self.validated_data['appointment_id']
        return appointment_id

            


class DoctorResaonSerializer(serializers.ModelSerializer):
    doctor_rej_reason = serializers.CharField()
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
            'appointment_time'
        ]


class SetPrepNurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'prep_nurse'
        ]