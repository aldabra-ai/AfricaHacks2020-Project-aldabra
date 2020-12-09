from django.contrib import admin
from django.db import DefaultConnectionProxy
from .models import  Hospital,Block,Room
from .models import Doctor,Speciality,Appointment,Nurse

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'hospital_type', 'rank',)
    list_filter = ('name', 'hospital_type', 'rank', 'address')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'room_number', 'room_type', 'block', 'availability', 'hospital')
    list_filter = ('hospital', 'availability')
    prepopulated_fields = {'slug': ('hospital','room_name','room_number','block',)}

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('hospital','block_name','block_floor','block_code')
    list_filter = ('hospital','block_name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','doctor_id','works_in','position')
    list_filter = ('name','trained_in','works_in','position')
    prepopulated_fields = {'slug': ('name','doctor_id',)}


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name','treatment')


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name','nurse_id','position','registered','current_employer')
    list_filter = ('name', 'position', 'current_employer',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'patient_name','hospital', 'prep_nurse', 'physician', 'start_dt_time','end_dt_time')
    list_filter = ('appointment_id', 'hospital','physician', 'start_dt_time','end_dt_time')
