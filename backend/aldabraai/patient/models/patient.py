from django.db import models
#from hospitaldb.models import Doctor
from django.urls import reverse
from django.conf import settings



class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    family_phone = models.CharField(max_length=20, blank=True)
    #user = models.ForeignKey('auth.User', related_name='patients', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})
