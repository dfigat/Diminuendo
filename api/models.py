from django.db import models

class Meeting(models.Model):
    project_id = models.IntegerField()
    team_id = models.IntegerField()
    leader_id = models.IntegerField()
    meeting_name = models.CharField(max_length=100)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()