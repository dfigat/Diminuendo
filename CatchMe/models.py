from django.db import models


class User(models.Model):
    id_user = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.fname + " " + self.lname


class Team(models.Model):
    id_team = models.AutoField(auto_created=True, primary_key=True)
    id_leader = models.ForeignKey(User, on_delete=models.CASCADE)
    tname = models.CharField(max_length=100)

    def __str__(self):
        return self.tname


class Project(models.Model):
    id_project = models.AutoField(auto_created=True, primary_key=True)
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    pstart = models.DateField()
    pend = models.DateField(null=True, blank=True)
    pdeadline = models.DateField()

    def __str__(self):
        return self.pname


class TeamMember(models.Model):
    id_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Team name: "+self.id_team.tname + "| First name: "+self.id_user.fname + "| Last name: "+self.id_user.lname


class Meeting(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_team = id_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    id_leader = id_leader = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting_name = models.CharField(max_length=100, null=True)
    meeting_date = models.DateField(null=True)
    meeting_time = models.TimeField(null=True)

    def __str__(self):
        return "Meeting name: "+self.id_team.tname
