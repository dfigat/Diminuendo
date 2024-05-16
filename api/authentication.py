from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from CatchMe.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            return user
        return None
