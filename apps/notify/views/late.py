from rest_framework.viewsets import ModelViewSet
from notify.models.late import Lateness
from notify.serializers.late import LatenessSerializer


class LatenessViewSet(ModelViewSet):
    queryset = Lateness.objects.all()
    serializer_class = LatenessSerializer

    def get_queryset(self):
        return Lateness.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)