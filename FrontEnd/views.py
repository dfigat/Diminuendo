from django.shortcuts import render, HttpResponse

# Create your views here.

def HomePage(request):
    return render(request, "home.html")

def Login(request):
    return render(request, "login.html")

def Register(request):
    return render(request, "register.html")