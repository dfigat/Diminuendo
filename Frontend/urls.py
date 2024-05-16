from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('/', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]