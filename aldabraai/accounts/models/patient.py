from django.conf import settings
from django.db import models
from .doctor import Doctor

class Patient(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField('Full Name', max_length=150)
    home_address = models.CharField('Home Address', max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    phone = models.CharField('Phone Number', max_length=20)
    family_or_emerg_phone = models.CharField('Family or Emergency Phone Number',max_length=20, blank=True)
    pcp = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name