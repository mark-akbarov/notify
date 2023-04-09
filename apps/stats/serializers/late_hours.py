from rest_framework import serializers


class LateHoursByMonthSerializer(serializers.Serializer):
    month = serializers.IntegerField()