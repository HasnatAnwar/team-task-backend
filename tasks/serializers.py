from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    # add these two field they will give me username and teamname 
    username = serializers.CharField(source="assigned_to.username", read_only=True)
    teamname = serializers.CharField(source="team.name", read_only=True)


    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "team",
            "assigned_to",
            "created_by",
            "status",
            "due_date",
            "created_at",
            
            # add them here
            "username",
            "teamname"
        ]
        # it will not be changed 
        read_only_fields = ["created_by"]