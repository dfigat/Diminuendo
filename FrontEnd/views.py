from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from Frontend.forms import RegisterForm

# Create your views here.

def HomePage(request):
    return render(request, "home.html")

def Login(request):
    return render(request, "login.html")

def Register(request):
    return render(request, "register.html")

def Reg(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Użytkownik został dodany")
    else:
        form = RegisterForm()

    return render(response, "reg.html", {"form": form})