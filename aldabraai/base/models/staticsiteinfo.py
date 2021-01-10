from django.db import models


class StaticSiteInfo(models.Model):
    company_name = models.CharField('Company Name', max_length=150)
    app_name = models.CharField('Application Name', max_length=150)
    app_summary = models.CharField('Application Summary', max_length=500)
    tag_line = models.CharField('Tag Line', max_length=500)
    date_founded = models.DateField('Date Founded')
    current_date = models.DateField(auto_now=True)


    # def __str__(self):
    #     self.app_name

    class Meta:
        verbose_name = 'Static Website Information'
        verbose_name_plural = 'Static Website Informations'

    

