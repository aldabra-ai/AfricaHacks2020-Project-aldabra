from django.contrib import admin
from .models import  Hospital,Block,Room

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


