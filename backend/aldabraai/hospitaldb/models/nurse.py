from django.db import models
from .hospital import Hospital

class RegisteredNurseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(registered=True)


class Nurse(models.Model):
    nurse_id = models.BigIntegerField()
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=250)
    registered = models.BooleanField(default=True)
    current_employer = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



