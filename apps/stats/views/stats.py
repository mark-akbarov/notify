from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from user.models.base import User
from notify.models import *
from stats.serializers.stats import StatSerializer, StatByMonthSerializer, StatsByUserSerializer

class StatisticsList(ListAPIView):
    serializer_class = StatSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class StatisticsByUserList(ListAPIView):
    serializer_class = StatsByUserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()


class StatisticsByMonth(APIView):
    def post(self, request):
        serializer = StatByMonthSerializer(data=request.data)
        if serializer.is_valid():
            month = serializer.validated_data['month']
            late = Lateness.objects.filter(user=request.user, created_datetime__month=month).count()
            warn = Warn.objects.filter(user=request.user, created_datetime__month=month).count()
            remote = Lateness.objects.filter(user=request.user, created_datetime__month=month).count()
            timeoff = Timeoff.objects.filter(user=request.user, created_datetime__month=month).count()
            stats_filter_by_month = {"late": late, "warn": warn, "remote": remote, "timeoff": timeoff}
            return Response({"stats_filter_by_month": stats_filter_by_month},)