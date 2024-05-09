from django.contrib import admin
from CatchMe.models import User
from CatchMe.models import Team
from CatchMe.models import Project
from CatchMe.models import TeamMember
from CatchMe.models import Meeting

admin.site.register(Meeting)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(User)