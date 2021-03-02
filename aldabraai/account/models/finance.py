from django.db import models
from django.conf import settings


class PatientBankDetail(models.Model):
    bank_name = models.CharField(max_length=500)
    account_name = models.CharField(max_length=350)
    account_number = models.CharField(max_length=11)
    branch_name = models.CharField(max_length=300)
    branch_code = models.CharField(max_length=6)
    swift_code = models.CharField(max_length=8)
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='bank_details', on_delete=models.CASCADE)


    def __str__(self):
        return self.account_name

class PatientInsurranceDetail(models.Model):
    insurrance_company = models.CharField(max_length=500)
    insurrance_name = models.CharField(max_length=300)
    insurrance_account_name = models.CharField(max_length=300)
    insurrance_account_no = models.CharField(max_length=12)
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='inssurance_details', on_delete=models.CASCADE)
    bank_details = models.OneToOneField(PatientBankDetail, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.insurrance_account_name

