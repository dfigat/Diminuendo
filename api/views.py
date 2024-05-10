from rest_framework import generics, status
from rest_framework.response import Response

from .views import *
from .serializers import *
from Frontend.forms import RegistrationForm


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def register_user(self, request):
        if request.method == 'POST':
            # form = RegistrationForm(request.POST)
            serializer =  UserSerializer
            if serializer.is_valid():
                first_name = serializer.cleaned_data['first_name']
                last_name = serializer.cleaned_data['last_name']
                email = serializer.cleaned_data['email']
                password = serializer.cleaned_data['password']
                
                user = User.objects.create(fname = first_name, lname = last_name, email = email, password = password)

                return Response({'msg': 'New account succesfully created!'}, status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Some functions for later if needed


class TeamList(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    # Some functions for later if needed


class TeamRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    # Some functions for later if needed


class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    # Some functions for later if needed


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    # Some functions for later if needed


class TeamMemberList(generics.ListCreateAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()

    # Some functions for later if needed


class TeamMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()

    # Some functions for later if needed


class MeetingList(generics.ListCreateAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()

    # Some functions for later if needed


class MeetingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()

    # Some functions for later if needed
