from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class AmongUsForm(UserCreationForm):
    email = forms.EmailField() #default: required=True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class CrewmateUpdateForm(forms.ModelForm):
    email = forms.EmailField() #default: required=True

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']