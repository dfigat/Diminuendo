from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = [
            'project_id',
            'team_id',
            'leader_id',
            'meeting_name',
            'meeting_date',
            'meeting_time',
        ]