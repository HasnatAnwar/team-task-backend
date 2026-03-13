from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from teams.models import Team
User = settings.AUTH_USER_MODEL


class Task(models.Model):

    STATUS_CHOICES = (
        ("pending","Pending"),
        ("in_progress","In Progress"),
        ("completed","Completed")
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="tasks")
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_tasks")
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")
    due_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)