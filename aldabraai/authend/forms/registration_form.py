from django.forms  import ModelForm, widgets
from django import forms

from ..models import User

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from ..models.user import (
    PROFILE_TYPE,
    GENDER,
)


class UserRegistrationForm(UserCreationForm):
    """
    Register a new user
    """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email =  forms.EmailField(label='Email')
    profile_type = forms.ChoiceField(label='Register As',choices=PROFILE_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    #user_id = forms.UUIDField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'profile_type',
            'gender',
            #'user_id',
            'password1', 
            'password2',
            ]

    def __init__(self, *args, **kwargs):
        """
        specify styles
        """

        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for fields in (
            self.fields['email'], 
            self.fields['first_name'], 
            self.fields['last_name'], 
            self.fields['gender'], 
            self.fields['profile_type'], 
            self.fields['password1'], 
            self.fields['password2']):
            fields.widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )


class UserOnboardingForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'date_of_birth',
            ]