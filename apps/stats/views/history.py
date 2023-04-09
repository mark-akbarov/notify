from rest_framework.generics import ListAPIView
from stats.serializers.history import HistorySerializer
from user.models.base import User


class HistoryList(ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)