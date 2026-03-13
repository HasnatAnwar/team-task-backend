from rest_framework import serializers
from .models import Team,TeamMember


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ["created_by"]
    # created by only one time created just it will not be changed

class TeamMemberSerializer(serializers.ModelSerializer):
    # add username to the teammember instance 
    # it will give me username along with team member details
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = TeamMember
        fields = [
            "id",
            "team",
            "user",
            "username",
            "role",
        ]