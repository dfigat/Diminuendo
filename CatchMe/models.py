from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import uuid

class CustomUserManager(UserManager):
    
    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'CatchMe_user'
        swappable = 'AUTH_USER_MODEL'
        # related_name = 'custom_groups'
        # related_query_name = 'custom_group'

    def __str__(self):
        return self.email


User._meta.get_field('groups').remote_field.related_name = 'custom_groups'
User._meta.get_field(
    'user_permissions').remote_field.related_name = 'custom_user_permissions'


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


class EmailVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.token)
