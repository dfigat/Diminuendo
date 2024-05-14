from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from Frontend.forms import RegistrationForm

# Create your views here.

def HomePage(request):
    return render(request, "home.html")

def Login(request):
    return render(request, "login.html")

def Register(request):
    return render(request, "register.html")

# def Reg(response):
#     if response.method == "POST":
#         form = RegistrationForm(response.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Użytkownik został dodany")
#     else:
#         form = RegistraForm()

#     return render(response, "reg.html", {"form": form})