from rest_framework import serializers
from notify.models.warn import Warn


class WarnSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Warn
        fields = ['pk', 'user', 'warning']
