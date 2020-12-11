from django.db import models



class Queue(models.Model):

    COMING_FOR = [
        ('APT', 'Appointment'),
        ('GEN', 'General Reason'),
        ('URG', 'Urgent Reason')
    ]

    
