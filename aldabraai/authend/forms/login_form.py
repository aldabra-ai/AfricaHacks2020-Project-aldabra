from django import forms

from django.contrib.auth import authenticate
from django.db.models import fields
from django.forms import widgets

from ..models import User


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]

        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

        def __init__(self, *args, **kwargs):
            """
            """

            super(LoginForm, self).__init__(*args, **kwargs)
            for field in (self.fields['email'], self.fields['password']):
                field.widget.attrs.update({
                    'class': 'form-control'
                })

        def clean(self):
            if self.is_valid():

                data = {
                    'email': self.cleaned_data.get('email'),
                    'password': self.cleaned_data.get('password')
                }

                if not authenticate(email=data['email'], password=data['password']):
                    raise forms.ValidationError('Invalid Login')

                    