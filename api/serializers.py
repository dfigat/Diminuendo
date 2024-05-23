from django.contrib.auth.hashers import make_password, check_password

from rest_framework import serializers, status

from CatchMe.models import *

import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

    def validate_first_name(self, value: str):
        if not value.isalpha():
            raise serializers.ValidationError(
                "First name must contain only letters")
        return value.lower().capitalize()

    def validate_last_name(self, value: str):
        parts = value.split('-')
        if not all(part.isalpha() for part in parts):
            raise serializers.ValidationError(
                "Last name must contain only letters and/or hyphens between each part")
        return '-'.join(part.lower().capitalize() for part in parts)

    def validate_email(self, value):
        value = value.lower()
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, value) is None:
            raise serializers.ValidationError(
                "Given e-mail is of incorrect format")
        elif User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered in database")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long")
        return value

    def create(self, validated_data):
        hashed_password = make_password(validated_data['password'])
        user = User(
            email=validated_data['email'],
            fname=validated_data['fname'],
            lname=validated_data['lname'],
            password=hashed_password,
        )
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ResendVerificationEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id_team', 'id_leader', 'tname']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('__all__')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('__all__')
