from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='Home'),
    path('login', views.Login, name='Login'),
    path('register', views.Register, name='Register')
]