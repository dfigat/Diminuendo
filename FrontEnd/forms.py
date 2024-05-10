from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from CatchMe.models import models, User


class RegistrationForm(forms.Form):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput())