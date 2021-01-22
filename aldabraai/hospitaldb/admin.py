from django.contrib import admin
from .models import  Hospital,Room,Block,Department,MedicalRecord,DoctorOffice,OfficeSchedule


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'address',
        'hospital_type',
        'rank',
    ]

    list_filter =  [
        'name', 
        'hospital_type',
        'rank',
    ]

    search_fields =  [
        'name', 
        'address',
        'hospital_type',
        'rank',
    ]

    list_per_page = 100

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'room_name', 
        'hospital',
        'room_type',
        'room_number',
        'block',
        'availability',
    ]

    list_filter = [
        'room_name', 
        'hospital',
        'room_type',
        'room_number',
        'block',
        'availability',
    ]

    search_fields =  [
        'room_name', 
        'hospital',
        'room_type',
        'room_number',
        'block',
        'availability',
    ]

    list_per_page = 100


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = [ 
        'hospital',
        'block_floor',
        'block_code',
    ]

    list_display = [ 
        'hospital',
        'block_floor',
        'block_code',
    ]

    list_display = [ 
        'hospital',
        'block_floor',
        'block_code',
    ]


    list_per_page = 100



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass



@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    pass



@admin.register(DoctorOffice)
class DoctorOfficeAdmin(admin.ModelAdmin):
    list_display = [
        'office_name',
        'office_owner',
        'hospital',
        'city',
        'state',
        'country',
        'zip_code'
    ]

    list_filter =  [
        'office_name',
        'office_owner', 
        'hospital',
        'first_consultation_fee',
        'city',
        'state',
        'country',
        'zip_code'
    ]

    search_fields =  [
        'office_name',
        'office_owner',  
        'hospital',
        'city',
        'state',
        'country',
        'zip_code'
    ]
    list_per_page = 100


@admin.register(OfficeSchedule)
class OfficeScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'office', 
        'availability',
        'start_time',
        'end_time'
    ]

    list_filter =  [
        'office', 
        'availability',
        'start_time',
        'end_time'
    ]

    search_fields =  [
        'office', 
        'availability',
        'start_time',
        'end_time'
    ]

    list_per_page = 100
