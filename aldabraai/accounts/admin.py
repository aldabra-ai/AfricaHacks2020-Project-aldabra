from django.contrib import admin
from .models import Patient,Doctor,DoctorSpecialization,DoctorSpecialization,DoctorQualification,Specialization,PatientReview,PatientBankDetail,PatientInsurranceDetail, AffiliatedHospital

@admin.register(Patient)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = [
        'owner', 
        'full_name', 
        'home_address', 
        'city', 
        'country', 
        'phone', 
        #'pcp'
        ]
    
    list_filter = [
        'owner', 
        'city', 
        'country', 
        #'pcp'
        ]


    list_per_page = 100

    search_fields = [
        'owner', 
        'full_name', 
        'city', 
        'country', 
        #'pcp'
        ]
@admin.register(Doctor)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = [
        'owner', 
        'doctor_id',
        'residing_hospital',
        'practicing_from',
        ]
    
    list_filter = [
        'owner', 
        'residing_hospital',  
        'practicing_from',
        ]

    list_per_page = 100

    search_fields = [
        'owner', 
        'residing_hospital',  
        'practicing_from',
        ]

    date_hierarchy = 'practicing_from'

@admin.register(DoctorQualification)
class DoctorQualificationAdmin(admin.ModelAdmin):
    list_display = [
        'doctor',
        'qualification_name',
        'institute_name',
        'procurement_year',
        ]
    
    list_filter = [
        'doctor',
        'qualification_name',
        'institute_name',
        'procurement_year',
        ]

    list_per_page = 100

    search_fields = [ 
        'doctor',
        'qualification_name',
        'institute_name',
        'procurement_year',
        ]

    date_hierarchy = 'procurement_year'

@admin.register(DoctorSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ['doctor',]
    list_filter = ['doctor',]
    search_fields = ['name', 'specialization']

    list_per_page = 100

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']

    list_per_page = 100

@admin.register(AffiliatedHospital)
class AffiliateHospitalAdmin(admin.ModelAdmin):
    list_display = [
        'affiliated_doctor',
        'hospital_name', 
        'affiliation_relationship',  
        'start_date',
        'end_date',
        ]
    
    list_filter = [
        'affiliated_doctor',
        'hospital_name', 
        'affiliation_relationship',  
        'start_date',
        'end_date',
        ]

    list_per_page = 100

    search_fields = [
        'affiliated_doctor',
        'hospital_name', 
        'affiliation_relationship',  
        'start_date',
        'end_date',
        ]

    date_hierarchy = 'start_date'

@admin.register(PatientReview)
class PatientReviewAdmin(admin.ModelAdmin):
    list_display = [
        'review_name',
        'owner', 
        'reviewed_doctor',  
        'anonymous_review',
        'overall_rating',
        'is_doctor_recommended',
        'review_date',
        ]
    
    list_filter = [
        'review_name',
        'owner', 
        'reviewed_doctor',  
        'anonymous_review',
        'overall_rating',
        'is_doctor_recommended',
        'review_date',
        ]

    list_per_page = 100

    search_fields = [
        'review_name',
        'owner', 
        'reviewed_doctor',  
        'anonymous_review',
        'overall_rating',
        'is_doctor_recommended',
        'review_date',
        ]

    date_hierarchy = 'review_date'


@admin.register(PatientBankDetail)
class PatientBankDetailAdmin(admin.ModelAdmin):
    list_display = [
        'bank_name',
        'patient', 
        'account_name',  
        'account_number',
        'branch_name',
        'branch_code',
        'swift_code',
        ]
    
    list_filter = [
        'bank_name',
        'patient', 
        'account_name',  
        'account_number',
        'branch_name',
        'branch_code',
        'swift_code',
        ]

    list_per_page = 100

    search_fields = [
        'bank_name',
        'patient', 
        'account_name',  
        'account_number',
        'branch_name',
        'branch_code',
        ]


@admin.register(PatientInsurranceDetail)
class PatientInsurranceDetailAdmin(admin.ModelAdmin):
    list_display = [
        'insurrance_company',
        'insurrance_name', 
        'insurrance_account_name',  
        'insurrance_account_no',
        'patient',
        ]
    
    list_filter = [
        'insurrance_company',
        'insurrance_name', 
        'insurrance_account_name',  
        'insurrance_account_no',
        'patient',
        ]

    list_per_page = 100

    search_fields = [
        'insurrance_company',
        'insurrance_name', 
        'insurrance_account_name',  
        'insurrance_account_no',
        'patient',
        ]

