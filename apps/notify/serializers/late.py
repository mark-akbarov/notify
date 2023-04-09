from rest_framework import serializers
from notify.models.late import Lateness


class LatenessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lateness
        fields = ['pk', 'hour', 'minutes']