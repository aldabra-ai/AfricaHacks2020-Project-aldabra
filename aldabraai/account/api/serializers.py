# framework imports
from rest_framework import serializers

# Patient Models
from ..models import (
                      Patient,
                      PatientBankDetail,
                      PatientReview,
                      PatientInsurranceDetail,
                      Doctor
                      )

# Doctor Models
from ..models import (
                      Doctor, 
                      DoctorQualification, 
                      DoctorSpecialization, 
                      Specialization
                      )

######################## PATIENT SERIALIZERS ##########################
class PatientDetailSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(read_only=True)
    full_name = serializers.ReadOnlyField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            "id",
            "full_name", 
            "home_address",
            "city",
            "country",
            "phone",
            "family_or_emerg_phone"
        ]

class PatientBankDetailSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PatientBankDetail
        fields = [
            "bank_name",
            "account_name",
            "account_number",
            "branch_name",
            "branch_code",
            "swift_code",
            "patient"
        ]

class PatientInsurranceDetailSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True)
    bank_details = PatientBankDetailSerializer(read_only=True)
    class Meta:
        model = PatientInsurranceDetail
        fields = [
            "insurrance_company",
            "insurrance_name",
            "insurrance_account_name",
            "insurrance_account_no",
            "patient",
            "bank_details"
        ]

class DoctorReviewSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    review_date = serializers.DateTimeField(read_only=True)
    review_state = serializers.ReadOnlyField()
    reviewed_doctor = serializers.PrimaryKeyRelatedField(read_only=True)
  
    class Meta:
        model = PatientReview
        fields = [
            "review_name",
            "owner",
            "reviewed_doctor",
            "anonymous_review",
            "wait_time_rating",
            "bedside_manner_rating",
            "overall_rating",
            "review",
            "is_doctor_recommended",
            "not_recommended_reason",
            "review_date",
            "publish",
            "review_state"

        ]
########################################## ****** ###################################

########################################## DOCTOR SERIALIZERS #######################
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