from django.contrib import admin
from .models import  Hospital,Room,Block,Department,MedicalRecord,DoctorOffice,OfficeSchedule


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass



@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass



@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    pass



@admin.register(DoctorOffice)
class DoctorOfficeAdmin(admin.ModelAdmin):
    pass



@admin.register(OfficeSchedule)
class OfficeScheduleAdmin(admin.ModelAdmin):
    pass