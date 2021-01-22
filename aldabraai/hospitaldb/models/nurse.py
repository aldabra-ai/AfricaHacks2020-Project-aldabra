from django.db import models
from .hospital import Hospital




class Nurse(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    nurse_id = models.CharField(max_length=7, unique=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name