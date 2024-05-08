from django.db import models

# Create your models here.
class user(models.Model):
    id_user = models.AutoField(auto_created = True, primary_key = True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    is_admin = models.BooleanField(default = False)



class team(models.Model):
    id_team = models.AutoField(auto_created = True, primary_key = True)
    id_leader = models.ForeignKey(user,on_delete = models.CASCADE,related_name = 'leader' )
    tname = models.CharField(max_length=100)


class project(models.Model):
    id_project = models.AutoField(auto_created = True, primary_key = True)
    id_team = models.ForeignKey(team,on_delete = models.CASCADE,related_name = 'team' )
    pname = models.CharField(max_length=50)
    pstart = models.DateField()
    pend = models.DateField()
    pdeadline = models.DateField()


class teamMember(models.Model):
    id_team = models.ForeignKey(team, on_delete = models.CASCADE,related_name = 'members')
    id_project = models.ForeignKey(project, on_delete = models.CASCADE,related_name = 'project')
    id_user = models.ForeignKey(user, on_delete = models.CASCADE,related_name = 'users')