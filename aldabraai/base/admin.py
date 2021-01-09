from django.contrib import admin
from .models import StaticSiteInfo, Feature, Sponsor


@admin.register(StaticSiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ['__all__']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['__all__']

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['__all__']
