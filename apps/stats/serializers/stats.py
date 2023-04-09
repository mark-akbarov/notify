from rest_framework import serializers
from user.models.base import User

class StatSerializer(serializers.ModelSerializer):
    late_count = serializers.SerializerMethodField()
    remote_count = serializers.SerializerMethodField()
    warn_count = serializers.SerializerMethodField()
    timeoff_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['late_count', 'remote_count', 'warn_count', 'timeoff_count']

    def get_late_count(self, obj):
        return obj.lateness.all().count()
    
    def get_remote_count(self, obj):
        return obj.remote_set.all().count()
    
    def get_warn_count(self, obj):
        return obj.warn_set.all().count()

    def get_timeoff_count(self, obj):
        return obj.timeoff_set.all().count()


class StatsByUserSerializer(StatSerializer):
    class Meta(StatSerializer.Meta):
        fields = StatSerializer.Meta.fields + ['username',]

    def get_username(self, obj):
        return obj.username


class StatByMonthSerializer(serializers.Serializer):
    month = serializers.IntegerField()