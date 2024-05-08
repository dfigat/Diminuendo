from rest_framework import serializers
from CatchMe.models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = [
            'id_project',
            'id_team',
            'id_leader',
            'meeting_name',
            'meeting_date',
            'meeting_time',
        ]
