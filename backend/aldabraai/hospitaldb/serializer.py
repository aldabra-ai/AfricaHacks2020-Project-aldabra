from django.db.models import fields
from rest_framework import serializers
from .models import Appointment,Speciality,Doctor,Nurse,Hospital,Room,Block


class HospitalSerializer(serializers.ModelSerializer):
    model = Hospital
    fields = [
        'name',
        'address',
        'hospital_type',
        'rank'
        ]

class BlockSerializer(serializers.ModelSerializer):
    model = Block
    fields = [
        'hospital', 
        'block_name', 
        'block_floor', 
        'block_code'
        ]

class RoomSerializer(serializers.ModelSerializer):
    model = Room
    fields = [
        'hospital', 
        'room_number', 
        'room_name', 
        'room_type', 
        'block', 
        'availability'
        ]

class DoctorSerializer(serializers.ModelSerializer):
    model = Doctor
    fields = [
        'doctor_id', 
        'name', 
        'works_in', 
        'position', 
        'trained_in', 
        'cert_date', 
        'cert_exp'
        ]

class SpecialitySerializer(serializers.ModelSerializer):
    model = Speciality
    fields = [
        'name', 
        'treatment'
        ]

class AppointmentSerializer(serializers.ModelSerializer):
    model = Appointment
    fields = [
        'appointment_id', 
        'patient_name', 
        'hospital', 
        'prep_nurse', 
        'appointment_for', 
        'physician',
        'start_dt_time',
        'end_dt_time',
        'examination_room'
         ]



