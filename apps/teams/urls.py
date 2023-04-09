# Django
from django.urls import path

# Project
from teams.views import ProjectDetailAPIView


urlpatterns = [
    path('<int:pk>/members/', ProjectDetailAPIView.as_view(), name='team-detail')
]