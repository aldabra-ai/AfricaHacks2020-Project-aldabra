#### REST FRAMEWORK ####
from rest_framework import serializers

#### MODELS ####
from ..models import Appointment


class RetrieveAppointmentSerializer(serializers.HyperlinkedModelSerializer):
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


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:patient-detail')
    booked_doctor_office = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    appointment_id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Appointment
        fields = [ 
            'id',
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


            


class DoctorResaonSerializer(serializers.HyperlinkedModelSerializer):
    doctor_rej_reason = serializers.CharField(min_length=20)
    class Meta:
        fields = [
            'doctor_rej_reason'
        ]


class RescheduleAppointmentSerializer(serializers.HyperlinkedModelSerializer):
    appointment_date = serializers.DateField()
    appointment_time = serializers.TimeField()
    
    class Meta:
        model = Appointment
        fields = [
            'appointment_date',
            'appointment_time',
            'prep_nurse'
        ]


class SetPrepNurseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'prep_nurse'
        ]

    
class BookedAppointmentSerializer(serializers.HyperlinkedModelSerializer):
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

class RequestedAppointmentSerializer(serializers.HyperlinkedModelSerializer):
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