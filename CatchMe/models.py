from django.db import models

# Create your models here.


class user(models.Model):
    id_user = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.fname + " " + self.lname


class team(models.Model):
    id_team = models.AutoField(auto_created=True, primary_key=True)
    id_leader = models.ForeignKey(user, on_delete=models.CASCADE)
    tname = models.CharField(max_length=100)

    def __str__(self):
        return self.tname


class project(models.Model):
    id_project = models.AutoField(auto_created=True, primary_key=True)
    id_team = models.ForeignKey(team, on_delete=models.CASCADE)
    pname = models.CharField(max_length=50)
    pstart = models.DateField()
    pend = models.DateField(null=True, blank=True)
    pdeadline = models.DateField()

    def __str__(self):
        return self.pname


class teamMember(models.Model):
    id_team = models.ForeignKey(team, on_delete=models.CASCADE)
    id_project = models.ForeignKey(project, on_delete=models.CASCADE)
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return "Nazwa zespołu: "+self.id_team.tname + "| Imie: "+self.id_user.fname + "| Nazwisko: "+self.id_user.lname


class Meeting(models.Model):
    id_project = models.ForeignKey(project, on_delete=models.CASCADE)
    id_team = id_team = models.ForeignKey(team, on_delete=models.CASCADE)
    id_leader = id_leader = models.ForeignKey(user, on_delete=models.CASCADE)
    meeting_name = models.CharField(max_length=100, null=True)
    meeting_date = models.DateField(null=True)
    meeting_time = models.TimeField(null=True)

    def __str__(self):
        return "Nazwa spotkania: "+self.id_team.tname
