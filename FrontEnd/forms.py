from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from CatchMe.models import models, User

class RegisterForm(forms.ModelForm):
    email = models.EmailField()
    fname = models.CharField()
    lname = models.CharField()
    
    
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        fields = [
            'fname',
            'lname',
            'email',
            'password',
            'password2'
        ]