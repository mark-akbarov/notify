# Project
from teams.models import Project
from .serializers import ProjectListSerializer
from user.serializers.user import UserListSerializer

# Rest Framework
from rest_framework import generics
from django.shortcuts import get_object_or_404


class ProjectDetailAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    search_fields = ['username', 'first_name', 'last_name', 'position__position']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        project = get_object_or_404(Project, pk=pk)
        return project.user.all()