from django.contrib import admin
from .models import StaticAppInfo

@admin.register(StaticAppInfo)
class StaticAppInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'app_name', 'web_url', 'date_founded',)