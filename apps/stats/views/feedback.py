from rest_framework.viewsets import ModelViewSet
from stats.models.feedback import Feedback
from stats.serializers.feedback import FeedbackSerializer


class FeedbackViewset(ModelViewSet):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        queryset = Feedback.objects.all()
        queryset = queryset.filter(to_user=self.request.user)
        return queryset