from django.db import models

class ActiveFeatureManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state='AS')

class BetaFeatureManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state='BS')

class Feature(models.Model):

    FEATURE_STATE = [
        ('AS', 'Active State'),
        ('BS', 'Beta State')
    ]

    name = models.CharField('Feature Name', max_length=150)
    summary = models.CharField(max_length=500)
    state = models.CharField('Feature State', max_length=50, choices=FEATURE_STATE, default=FEATURE_STATE[1])
    # default manager
    objects = models.Manager()
    # custom managers
    active_features = ActiveFeatureManager()
    beta_features = BetaFeatureManager()


    def __str__(self):
        return self.name