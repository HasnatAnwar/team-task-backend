from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Team,TeamMember
from .serializers import TeamSerializer,TeamMemberSerializer


class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    # Return only teams where the current user is a member
    def get_queryset(self):
        return Team.objects.filter(members__user=self.request.user)

    # Save team with the logged-in user as creator
    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        
        # Add the creator as an admin member of the team
        TeamMember.objects.create(
            team=team,
            user=self.request.user,
            role="admin"
        )


class TeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMemberSerializer
    permission_classes = [IsAuthenticated]

    # Return members of this team only if the user belongs to the team
    def get_queryset(self):
        team_id = self.kwargs.get("team_pk")
        return TeamMember.objects.filter(
            team_id=team_id,
            team__members__user=self.request.user
        )
    # Add member to the team using team id from URL
    def perform_create(self, serializer):
        serializer.save(team_id=self.kwargs["team_pk"])

