# Rest Framework
from rest_framework import serializers

# Project
from teams.models import Project


class ProjectListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='team-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Project
        fields = ['url', 'id', 'name',]