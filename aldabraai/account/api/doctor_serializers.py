from ..models import Doctor, DoctorQualification, DoctorSpecialization, Specialization
from rest_framework import serializers


class DoctorDetailSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    doctor_id = serializers.CharField(max_length=10)
    practicing_from = serializers.DateField()

    class Meta:
        fields = [
            'full_name',
            'doctor_id',
            'residing_hospitals',
            'practicing_from',
        ]


class DoctorQualificationSerializer(serializers.ModelSerializer):
    qualification_name = serializers.CharField(max_length=700)
    institute_name = serializers.CharField(max_length=700)
    procurement_year = serializers.DateField()

    class Meta:
        fields = [
            'qualification_name',
            'institute_name',
            'procurement_year'
        ]

class DoctorSpecializationSerializer(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField(queryset=Specialization.objects.all(), many=True)

    class Meta:
        fields = [
            'specializtion'
        ]