from django.db import models
from .hospital import Hospital



class Nurse(models.Model):
    nurse_id = models.BigIntegerField()
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=250)
    registered = models.BooleanField(default=True)
    current_employer = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



