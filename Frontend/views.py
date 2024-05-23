from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from Frontend.forms import RegistrationForm

# Create your views here.


def home_page(request):
    return render(request, 'home.html')

def Events(request):
    return render(request, 'events.html')

def Projects(request):
    return render(request,'projects.html')

# def Reg(response):
#     if response.method == "POST":
#         form = RegistrationForm(response.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Użytkownik został dodany")
#     else:
#         form = RegistraForm()

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')

def resend_verification_email(request):
    return render(request, 'resend-verification-email.html')
