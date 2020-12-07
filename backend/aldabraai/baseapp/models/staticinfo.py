from django.db import models


class StaticAppInfo(models.Model):
    company_name = models.CharField(max_length=150)
    app_name = models.CharField(max_length=150)
    webapp_url = models.URLField(max_length=50)
    date_founded = models.DateField()
    logo = models.FileField(upload_to='', blank=True)
    #address

    def __str__(self):
        return self.app_name
    
    class Meta:
        verbose_name = 'Static Application Information'
        verbose_name_plural = 'Static Application Informations'