from django.urls import path

from .views import *

urlpatterns = [
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('team/', TeamList.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamRetrieveUpdateDestroy.as_view(), name='team-detail'),

    path('project/', ProjectList.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),

    path('team-member/', TeamMemberList.as_view(), name='team-member-list'),
    path('team-member/<int:pk>/', TeamMemberRetrieveUpdateDestroy.as_view(), name='team-member-detail'),

    path('meeting/', MeetingList.as_view(), name='meeting-list'),
    path('meeting/<int:pk>/', MeetingRetrieveUpdateDestroy.as_view(), name='meeting-detail'),
]
