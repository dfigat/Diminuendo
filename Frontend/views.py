from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from CatchMe.models import User
from Frontend.forms import RegistrationForm


def home_page(request):
    return render(request, 'home.html')


def Events(request):
    return render(request, 'events.html')


def Projects(request):
    return render(request, 'projects.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    return render(request, 'register.html')


def resend_verification_email(request):
    return render(request, 'resend-verification-email.html')


@login_required
def user_profile(request, id):
    profile_user = get_object_or_404(User, id_user=id)
    is_owner = request.user == profile_user
    return render(request, 'profile.html', {'profile_user': profile_user, 'is_owner': is_owner})
