from django.urls import path
from rest_framework.routers import DefaultRouter
from stats.views.history import HistoryList
from stats.views.feedback import FeedbackViewset
from stats.views.stats import StatisticsList, StatisticsByMonth, StatisticsByUserList
from stats.views.late_hours import LateHoursView, LateHoursByMonthAPIView


router = DefaultRouter()
router.register('feedback', FeedbackViewset, basename='feedback')

urlpatterns = [
    path('', StatisticsList.as_view()),
    path('late_hours/', LateHoursView.as_view()),
    path('late_hours_by_month/', LateHoursByMonthAPIView.as_view()),    
    path('stats_by_user/', StatisticsByUserList.as_view()),
    path('stats_by_month/', StatisticsByMonth.as_view()),
    path('history/', HistoryList.as_view()),
    # path('work_hours/', WorkHoursAPIView.as_view()),
]

urlpatterns += router.urls