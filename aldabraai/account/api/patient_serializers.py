from rest_framework import serializers
from ..models import Patient,PatientBankDetail,PatientReview,PatientInsurranceDetail


class PatientDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(read_only=True)
    full_name = serializers.ReadOnlyField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id',
            'full_name', 
            'home_address',
            'city',
            'country',
            'phone',
            'family_or_emerg_phone'
        ]

class PatientBankDetailSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PatientBankDetail
        fields = [
            'bank_name',
            'account_name',
            'account_number',
            'branch_name',
            'branch_code',
            'swift_code',
            'patient'
        ]

class PatientInsurranceDetailSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    bank_details = PatientBankDetailSerializer(read_only=True)
    class Meta:
        model = PatientInsurranceDetail
        fields = [
            'insurrance_company',
            'insurrance_name',
            'insurrance_account_name',
            'insurrance_account_no',
            'patient',
            'bank_details'
        ]


class PatientReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    review_date = serializers.DateTimeField(read_only=True)
    review_state = serializers.ReadOnlyField()
    class Meta:
        model = PatientReview
        fields = [
            'review_name',
            'owner',
            'reviewed_doctor',
            'anonymous_review',
            'wait_time_rating',
            'bedside_manner_rating',
            'overall_rating',
            'review',
            'is_doctor_recommended',
            'not_recommended_reason',
            'review_date',
            'publish',
            'review_state'

        ]
