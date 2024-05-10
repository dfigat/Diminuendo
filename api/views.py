from rest_framework import generics, status
from .views import *
from .serializers import *


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # some functions for later


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # some functions for later


class TeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    # some functions for later


class TeamRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    # some functions for later


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    # some functions for later


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    # some functions for later


class TeamMemberList(generics.ListCreateAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()

    # some functions for later


class TeamMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()

    # some functions for later


class MeetingList(generics.ListCreateAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()

    # some functions for later


class MeetingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()

    # some functions for later
