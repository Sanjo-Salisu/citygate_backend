# management/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import GalleryImage, ManagementProfile   # FIXED: import your models


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class ManagementProfileForm(forms.ModelForm):
    class Meta:
        model = ManagementProfile
        fields = ['name', 'title','about', 'profile_pic']

