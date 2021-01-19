from django.db import models
from django.conf import settings
from .doctor import Doctor




class PatientReview(models.Model):

    RECOMMENDED_CHOICE = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]

    review_name = models.CharField('The review name or summary', max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reviewed_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    is_review_anonymous = models.BooleanField(default=False)
    wait_time_rating = models.FloatField(max_length=3, blank=True)
    bedside_manner_rating = models.FloatField(max_length=3, blank=True)
    overall_rating = models.FloatField(max_length=5)
    review = models.TextField(max_length=4000, blank=True)
    is_doctor_recommended = models.CharField(max_length=1, choices=RECOMMENDED_CHOICE, default=RECOMMENDED_CHOICE[0])
    not_recommended_reason = models.TextField('A Reason for not recommending this Doctor', max_length=2000)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_name


    class Meta:
        ordering = ['review_name']

        
