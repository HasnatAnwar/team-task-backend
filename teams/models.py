from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey( User,on_delete=models.CASCADE,related_name="created_teams")
    created_at = models.DateTimeField(auto_now_add=True)


class TeamMember(models.Model):

    ROLE_CHOICES = (
        ("admin","Admin"),
        ("member","Member")
    )

    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="members")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default="member")
    joined_at = models.DateTimeField(auto_now_add=True)