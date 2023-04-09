from rest_framework import serializers
from stats.models.feedback import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['pk', 'to_user', 'title', 'body']