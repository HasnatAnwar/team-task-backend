from django.contrib import admin

# Register your models here.
from.models import Team , TeamMember


admin.site.register((Team,TeamMember))