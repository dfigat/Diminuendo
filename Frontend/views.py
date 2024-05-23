from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from Frontend.forms import RegistrationForm

# Create your views here.


def home_page(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')

def resend_verification_email(request):
    return render(request, 'resend-verification-email.html')
