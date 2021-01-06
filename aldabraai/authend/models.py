from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class AldabraUserManager(BaseUserManager):

    def create_user(self, first_name,last_name,email,username,date_of_birth,profile_type,password=None):
        """
        Creates and saves user with the given parameters:
        first_name,last_name,email,username,date_of_birth,profile_type,password.
        """

        if not (email,username):
            raise  ValueError('User must have an email address, username and profile_type')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_type=profile_type
            )  

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,first_name,last_name,username,date_of_birth,profile_type,password=None):
        """
        creates a superuser
        """

        user = self.create_user(
            email,
            first_name,
            last_name,
            username=username,
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

    first_name = models.CharField('Users First Name', max_length=200)
    last_name = models.CharField('Users Last Name', max_length=200)
    date_of_birth = models.DateField('Users Date Of Birth')
    username = models.CharField('Users Username', max_length=300, unique=True)
    email = models.EmailField('Users Email Address', unique=True)
    profile_type = models.CharField(max_length=10, choices=PROFILE_TYPE)

    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AldabraUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['email','first_name', 'last_name', 'date_of_birth', 'profile_type']

    def __str__(self):
        return self.username
    
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
    

    # def is_doctor(self):
    #     if self.profile_type == 'DR':
    #         return True
    #     else:
    #         False
    #     return self.is_doctor()
        
    # def is_patient(self):
    #     if self.profile_type == 'PT':
    #         return True
    #     else:
    #         False
    #     return self.is_patient()

    