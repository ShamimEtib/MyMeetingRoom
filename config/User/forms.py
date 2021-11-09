from django import forms
from django.db import models
from django.forms import fields, widgets
from API.models import User


class CreateUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email','password',]
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginUserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','password',]
        widgets = {
            'password': forms.PasswordInput(),
        }
