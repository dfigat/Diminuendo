from django.urls import path
from . import views

from api.views import VerifyEmailView, ResendVerificationEmailView

urlpatterns = [

    path('events/', views.Events, name='events'),
    path('projects/', views.Projects, name='projects'),
    path('', views.home_page, name='home'),
    path('/', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('resend-verification-message/', views.resend_verification_email, name='resend-verification-email'),
    path('verify-email/<uuid:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification-email/', ResendVerificationEmailView.as_view(), name='resend-verification-email'),

]