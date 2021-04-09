from rest_framework.relations import StringRelatedField
from ..models import DoctorOffice,OfficeSchedule, Hospital,MedicalRecord
from rest_framework import serializers


class OfficeScheduleSerializer(serializers.ModelSerializer):
    office = serializers.StringRelatedField()
    class Meta:
        model = OfficeSchedule
        fields = [
            'pk',
            'office',
            'day_available',
            'start_time',
            'end_time',
            'availability',
            'reason_for_unavailability'
        ]



class DoctorOfficeSerializer(serializers.ModelSerializer):
    office_owner = serializers.PrimaryKeyRelatedField(read_only=True)
    hospital = serializers.StringRelatedField()
    appointments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = DoctorOffice
        fields = [
            'id',
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
            'appointments'
        ]





