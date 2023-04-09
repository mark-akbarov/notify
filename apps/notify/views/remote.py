from rest_framework.viewsets import ModelViewSet
from notify.models.remote import Remote
from notify.serializers.remote import RemoteSerializer


class RemoteViewSet(ModelViewSet):
    serializer_class = RemoteSerializer

    def get_queryset(self):
        queryset = Remote.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        user.work_type = 'Remote'
        serializer.save(user=user)