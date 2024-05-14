from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('/', views.HomePage, name='home'),
    path('home/', views.HomePage, name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
]