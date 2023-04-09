from rest_framework.viewsets import ModelViewSet
from notify.models.timeoff import Timeoff
from notify.serializers.timeoff import TimeoffSerializer


class TimeoffViewSet(ModelViewSet):
    serializer_class = TimeoffSerializer

    def get_queryset(self):
        queryset = Timeoff.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        user.work_type = 'Timeoff'
        serializer.save(user=user)