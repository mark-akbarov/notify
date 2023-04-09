from rest_framework import serializers
from notify.models.timeoff import Timeoff


class TimeoffSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Timeoff
        fields = ['pk', 'user', 'timeoff', 'date', 'reason']