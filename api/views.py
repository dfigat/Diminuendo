from rest_framework import generics
from .serializers import MeetingSerializer
from CatchMe.models import Meeting

class MeetingListCreate(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer