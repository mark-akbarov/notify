from django.urls import path
from rest_framework.routers import DefaultRouter
from user.views.login import LoginAPIView
from user.views.mac import MacAPIView
from user.views.user import (
    UserViewSet, 
    BirthdayListAPIView, 
    ProfileRetrieveAPIView, 
    GetEmploymentStatus
)

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('birthday/', BirthdayListAPIView.as_view()),
    path('devices/', MacAPIView.as_view()),
    path('profile/', ProfileRetrieveAPIView.as_view()),
    path('isemployed/<int:pk>/', GetEmploymentStatus.as_view())
]

urlpatterns += router.urls