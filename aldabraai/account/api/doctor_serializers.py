from ..models import Doctor, DoctorQualification, DoctorSpecialization, Specialization
from rest_framework import serializers


class DoctorDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    doctor_id = serializers.CharField(max_length=10)
    practicing_from = serializers.DateField()

    class Meta:
        model = Doctor
        fields = [
            'id',
            'full_name',
            'doctor_id',
            'residing_hospital',
            'practicing_from',
        ]


class DoctorQualificationSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True)
    qualification_name = serializers.CharField(max_length=700)
    institute_name = serializers.CharField(max_length=700)
    procurement_year = serializers.DateField()

    class Meta:
        model = DoctorQualification
        fields = [
            'doctor',
            'qualification_name',
            'institute_name',
            'procurement_year'
        ]

class DoctorSpecializationSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = DoctorSpecialization
        fields = [
            'doctor',
            'specialization'
        ]