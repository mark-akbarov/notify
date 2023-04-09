from rest_framework import serializers
from notify.models.remote import Remote


class RemoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Remote
        fields = ['pk', 'user', 'date', 'reason']
