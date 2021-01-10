from django.contrib import admin
from .models import StaticSiteInfo, Feature, Sponsor

@admin.register(StaticSiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = [
            'company_name',
            'app_name','app_summary',
            'tag_line','date_founded',
            'current_date'
            ]


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'summary',
            'state',
            ]

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'logo',
            'website_url',
        ]
