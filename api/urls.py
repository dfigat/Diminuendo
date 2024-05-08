from django.urls import path
from .views import MeetingListCreate

urlpatterns = [
    path('meetings/', MeetingListCreate.as_view(), name='meeting-list-create')
]