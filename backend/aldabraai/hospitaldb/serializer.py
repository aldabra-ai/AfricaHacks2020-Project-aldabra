from rest_framework import serializers
from .models import Appointment,Speciality,Doctor,Nurse,Hospital,Room,Block


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = [
            'name',
            'address',
            'hospital_type',
            'rank',
            ]

class BlockSerializer(serializers.ModelSerializer):
    hospital = serializers.PrimaryKeyRelatedField(many=True, queryset=Hospital.objects.all())
    class Meta:
        model = Block
        fields = [
            'hospital', 
            'block_name', 
            'block_floor', 
            'block_code',
        ]

class RoomSerializer(serializers.ModelSerializer):
    hospital = serializers.PrimaryKeyRelatedField(many=True, queryset=Hospital.objects.all())
    block = serializers.PrimaryKeyRelatedField(many=True, queryset=Block.objects.all())
    class Meta:
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
    works_in = serializers.PrimaryKeyRelatedField(many=True, queryset=Hospital.objects.all())
    trained_in = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = [
                'doctor_id', 
                'name', 
                'works_in', 
                'works_in_id',
                'position', 
                'trained_in', 
                'cert_date', 
                'cert_exp'
        ]

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['name', 'treatment']

class NurseSerializer(serializers.ModelSerializer):
    current_employer = serializers.PrimaryKeyRelatedField(many=True, queryset=Hospital.objects.all())
    class Meta:
        model = Nurse
        fields = [
            'nurse_id',
            'name',
            'position',
            'registered',
            'current_employer'
        ]

class AppointmentSerializer(serializers.ModelSerializer):
    physician = serializers.PrimaryKeyRelatedField(many=True, queryset=Doctor.objects.all())
    hospital = serializers.PrimaryKeyRelatedField(many=True, queryset=Hospital.objects.all())
    prep_nurse = serializers.PrimaryKeyRelatedField(many=True, queryset=Nurse.objects.all())
    class  Meta:
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



