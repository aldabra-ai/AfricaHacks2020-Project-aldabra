from rest_framework.relations import StringRelatedField
from ..models import DoctorOffice,OfficeSchedule, Hospital,MedicalRecord
from rest_framework import serializers
from authend.models import User


class OfficeScheduleSerializer(serializers.ModelSerializer):
    office = serializers.StringRelatedField()
    class Meta:
        model = OfficeSchedule
        fields = [
            'office',
            'day_available',
            'start_time',
            'end_time',
            'availability',
            'reason_for_unavailability'
        ]



class DoctorOfficeSerializer(serializers.ModelSerializer):
    office_owner = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())
    hospital = serializers.StringRelatedField()
    office_schedule = OfficeScheduleSerializer(many=True)
    appointments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = DoctorOffice
        fields = [
            'office_owner',
            'office_name',
            'hospital',
            'first_consultation_fee',
            'follow_up_cons_fee',
            'street_address',
            'city',
            'state',
            'country',
            'zip_code',
            'office_schedule',
            'appointments'
        ]





