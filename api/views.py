from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .views import *
from .serializers import *
from Frontend.forms import RegistrationForm


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['fname'] = serializer.validated_data['fname'].capitalize()
            last_name_parts = serializer.validated_data['lname'].split('-')
            serializer.validated_data['lname'] = '-'.join(
                part.lower().capitalize() for part in last_name_parts)
            serializer.save()
            return Response({'msg': 'New account successfully created!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                return Response({'msg': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'msg': 'E-mail or password is wrong'}, status=status.HTTP_401_UNAUTHORIZED)

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
