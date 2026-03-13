from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # third party filter library
    filter_backends = [DjangoFilterBackend]
    # where we can filter
    filterset_fields = ["team","assigned_to"]

    def get_queryset(self):
        return Task.objects.filter(team__members__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)