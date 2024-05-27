from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .views import *
from .serializers import *
from CatchMe.models import EmailVerificationToken
from Frontend.forms import RegistrationForm
from Diminuendo.settings import DEFAULT_FROM_EMAIL

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        password = request.data['password']
        password_verify = request.data['password_verify']
        request.data['fname'] = request.data['fname'].lower().capitalize()
        parts = request.data['lname'].split('-')
        request.data['lname'] = '-'.join(part.lower().capitalize() for part in parts)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid() and password == password_verify:
            user = serializer.save(is_active=False)
            token = EmailVerificationToken.objects.create(user=user)
            verification_url = f'{request.scheme}://{request.get_host()}/verify-email/{token.token}/'
            send_mail(
                'Verify your e-mail address',
                f'Hello, {user.fname} {user.lname}!\n'
                f'Please click the link to verify your email: {verification_url},\n\n'
                f'This message is generated automatically. Please, do not respond to it!',
                DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return Response({'msg': 'New account created. Verify your e-mail!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def get(self, request, token):
        verification_token = get_object_or_404(
            EmailVerificationToken, token=token)
        user = verification_token.user
        user.is_active = True
        user.save()
        verification_token.delete()
        return redirect('/')


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email'].lower()
            password = serializer.validated_data['password']

            try:
                user = authenticate(request, email=email, password=password)
            except:
                user = None
            if user is not None:
                if user.is_active:  # Check if the user's email is verified
                    login(request, user)
                    return Response({'msg': 'Login successful'}, status=status.HTTP_200_OK)
                return Response({'msg': 'E-mail not verified. Please verify your e-mail'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'msg': 'E-mail or password is wrong'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Logout successful'}, status=status.HTTP_200_OK)


class ResendVerificationEmailView(APIView):
    def post(self, request):
        serializer = ResendVerificationEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                if user != None and not user.is_active:
                    token, created = EmailVerificationToken.objects.get_or_create(
                        user=user)
                    verification_url = f'{request.scheme}://{request.get_host()}/verify-email/{token.token}/'
                    send_mail(
                        'Verify your e-mail address',
                        f'Hello, {user.fname} {user.lname}!\n'
                        f'Please click the link to verify your email: {verification_url},\n\n'
                        f'This message is generated automatically. Please, do not respond to it!',
                        DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )
            except Exception as e:
                print(e)
            return Response({'msg': 'If account exists and is unauthorized, e-mail sent'}, status=status.HTTP_200_OK)
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
