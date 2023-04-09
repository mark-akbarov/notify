import datetime
from django.db.models import Sum, F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from notify.models.late import Lateness
from stats.serializers.late_hours import LateHoursByMonthSerializer


class LateHoursView(APIView):
    queryset = User.objects.all()
    
    def get(self, request):
        late = Lateness.objects.filter(
            user=request.user,
            created_datetime__year=datetime.date.today().year
            )\
            .values(month=F("created_datetime__month")) \
            .annotate(hours=Sum('total')) \
            .filter(hours__gt=0).order_by("created_datetime__month")
        statistics = {"late hours": late}
        return Response(statistics, status=status.HTTP_200_OK)
    

class LateHoursByMonthAPIView(APIView):
    def post(self, request):
        serializer = LateHoursByMonthSerializer(data=request.data)
        if serializer.is_valid():
            month = serializer.validated_data['month']
            late_hours_by_month = Lateness.objects.filter(
                user=request.user,\
                created_datetime__month=month,\
                created_datetime__year=datetime.date.today().year
                )\
                .values(month=F("created_datetime__month"))\
                .annotate(hours=Sum('total')).filter(hours__gt=0)\
                .order_by("created_datetime__month")
            late_hours = {"late_hours_by_month": late_hours_by_month}
        return Response(late_hours, status=status.HTTP_200_OK)