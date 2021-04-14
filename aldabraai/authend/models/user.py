from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.shortcuts import reverse

from django.contrib.auth.models import Group

class PatientUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(profile_type='PT')

class DoctorUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(profile_type='DR')
class AldabraUserManager(BaseUserManager):

    def create_user(self,email,identifier,date_of_birth,profile_type,password=None):
        """
        Creates and saves user with the given parameters:
        first_name,last_name,email,identifier,date_of_birth,profile_type,password.
        """

        if not email:
            raise  ValueError('User must have an email address, identifier and profile_type')

        user = self.model(
            email=email,
            identifier=identifier,
            date_of_birth=date_of_birth,
            profile_type=profile_type
            )  
        
        
        user.set_password(password)

        if user.profile_type == 'DR':
            user.is_patient = False
            user.is_doctor = True
            user.save(using=self._db)
        return user

    def create_superuser(self, email,identifier,date_of_birth,profile_type,password=None):
        """
        creates a superuser
        """

        user = self.create_user(
            email,
            identifier=identifier,
            date_of_birth=date_of_birth,
            password=password,
            profile_type=profile_type,
            )

        user.is_admin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):

    PROFILE_TYPE = [
        ('PT', 'Patient'),
        ('DR', 'Doctor'),
    ]

    first_name = models.CharField('First Name', max_length=200, blank=True)
    last_name = models.CharField('Last Name', max_length=200, blank=True)
    date_of_birth = models.DateField('Date Of Birth', help_text='YYY-MMM-DDD')
    identifier = models.CharField('Username', max_length=300, unique=True)
    email = models.EmailField('Email Address', unique=True)
    profile_type = models.CharField(max_length=10, choices=PROFILE_TYPE, default=PROFILE_TYPE[0])

    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)

    objects = AldabraUserManager()

    patient_users= PatientUserManager()
    doctor_users= DoctorUserManager()

    groups = models.ManyToManyField(Group, blank=True)

    USERNAME_FIELD = 'identifier'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['email','date_of_birth','profile_type']

    def __str__(self):
        return self.identifier
    
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def slug(self):
        slug = models.SlugField(default=self.identifier, unique=True)
        return slug
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True
    
    def has_module_perms(self, app_label):
        "Does the user has permissions to view app_label"
        return True

    @property
    def is_staff(self):
        "Is user a staff or member"
        return self.is_admin
    
    @property
    def is_doctor_or_patient(self):
        if self.is_doctor:
             return 'A Doctor'
        else:
            return 'A Patient'

    def get_absolute_url(self):
        if self.is_doctor:
            return reverse('accounts:doctor-detail', kwargs={'slug': self.slug})
        elif self.is_patient:
            return reverse('accounts:patient-detail', kwargs={'slug': self.slug})
