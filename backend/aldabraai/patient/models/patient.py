from django.db import models
from hospitaldb.models import Doctor



class Patient(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    pcp = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    family_phone = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
