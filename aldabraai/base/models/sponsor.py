from django.db import models


class Sponsor(models.Model):
    name = models.CharField('Sponsor Name', max_length=150)
    logo = models.URLField()
    website_url = models.URLField('Website URL')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] 
