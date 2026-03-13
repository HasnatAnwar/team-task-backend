
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TeamViewSet, TeamMemberViewSet

# a third party for nested router for this approach
from rest_framework_nested.routers import NestedDefaultRouter


# Main router for teams
router = DefaultRouter()
router.register('', TeamViewSet, basename='teams')

# Nested router for team members
# This creates routes like /teams/{team_id}/members/
teams_router = NestedDefaultRouter(router, '', lookup='team')
teams_router.register(r'members', TeamMemberViewSet, basename='team-members')

# /teams/1/members/
# /teams/1/members/5/
# in this way these routes works.


urlpatterns = [
    path("", include(router.urls)),
    path("", include(teams_router.urls)),
]