from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','identifier','first_name', 'last_name', 'date_of_birth', 'profile_type')

    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 != password2:
            raise forms.ValidationError("Passwords dont't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','identifier','first_name', 'last_name', 'date_of_birth','gender', 'profile_type','password','is_active','is_admin', 'is_doctor','is_patient')

    def clean_password(self):

        return self.initial['password']



class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email','first_name', 'last_name', 'date_of_birth', 'profile_type')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password','user_id')}),
        ('Personal Info', {'fields': ('identifier','first_name', 'last_name', 'date_of_birth','gender',)}),
        ('Permissions', {'fields': ('is_admin', 'is_doctor', 'is_patient')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','identifier','first_name', 'last_name', 'date_of_birth', 'profile_type','password1', 'password2'),
        }),
    )

    search_fields = ('email','identifier','first_name','profile_type')
    ordering = ('email','identifier','profile_type',)
    filter_horizontal = ()



admin.site.register(User, UserAdmin)


#admin.site.register(Group)



