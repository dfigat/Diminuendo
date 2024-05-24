from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from api.views import VerifyEmailView, ResendVerificationEmailView

urlpatterns = [

    path('events/', Events, name='events'),
    path('projects/', Projects, name='projects'),
    path('', home_page, name='home'),
    path('/', home_page, name='home'),
    path('home/', home_page, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('resend-verification-message/', resend_verification_email, name='resend-verification-email'),
    path('verify-email/<uuid:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification-email/', ResendVerificationEmailView.as_view(), name='resend-verification-email'),
    path('user/<int:id>/', user_profile, name='user_profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]