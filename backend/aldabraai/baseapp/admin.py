from django.contrib import admin
from .models import StaticAppInfo

@admin.register(StaticAppInfo)
class StaticAppInfoAdmin(admin.ModelAdmin):
    pass