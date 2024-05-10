from rest_framework import viewsets

from .models import *
from .serializers import *

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer