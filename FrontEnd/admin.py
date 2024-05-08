from django.contrib import admin
from CatchMe.models import user
from CatchMe.models import teamMember
from CatchMe.models import project
from CatchMe.models import team
# Register your models here.
admin.site.register(user)
admin.site.register(team)
admin.site.register(teamMember)
admin.site.register(project)

