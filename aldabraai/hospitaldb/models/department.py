from django.db import models
from .hospital import Hospital
from .hospital import Block


class Department(models.Model):
        name = models.CharField(max_length=250)
        hod = models.CharField(max_length=300)
        hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
        block = models.ForeignKey(Block, on_delete=models.PROTECT)
        department_id = models.CharField(max_length=12)
   
        def __str__(self):
             return self.name