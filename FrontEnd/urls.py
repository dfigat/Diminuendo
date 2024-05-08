from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='Home'),
    path('/', views.HomePage, name='Home'),
    path('Login', views.Login, name='Login'),
    path('register', views.Register, name='Register')
]