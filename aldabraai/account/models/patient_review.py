from django.db import models
from django.conf import settings
from django.db.models.fields import related
from .doctor import Doctor




class PatientReview(models.Model):

    REVIEW_STATE = [
        ('PUB', 'Published'),
        ('DFT', 'Draft'),
    ]

    RECOMMENDED_CHOICE = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]

    review_name = models.CharField('The review name or summary', max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    reviewed_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    anonymous_review = models.BooleanField(default=False)
    wait_time_rating = models.FloatField(max_length=3, blank=True)
    bedside_manner_rating = models.FloatField(max_length=3, blank=True)
    overall_rating = models.FloatField(max_length=5)
    review = models.TextField(max_length=4000, blank=True)
    is_doctor_recommended = models.CharField(max_length=5, choices=RECOMMENDED_CHOICE, default=RECOMMENDED_CHOICE[0][0])
    not_recommended_reason = models.TextField('A Reason for not recommending this Doctor', max_length=2000)
    review_date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    review_state = models.CharField(max_length=10, choices=REVIEW_STATE, default=REVIEW_STATE[0][0])

    def __str__(self):
        return self.review_name


    class Meta:
        ordering = ['review_name']

        
