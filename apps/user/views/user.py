from datetime import datetime
from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from user.models import User
from user.serializers.user import (
    UserSerializer, 
    UserListSerializer, 
    BirthdayListSerializer, 
    ProfileSerializer
)


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    search_fields = ['username', 'first_name', 'last_name', 'position__position']

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserSerializer


class BirthdayListAPIView(generics.ListAPIView):
    serializer_class = BirthdayListSerializer
    search_fields = ['username', 'first_name', 'last_name', 'position__position']

    def get_queryset(self):
        return User.objects.filter(birthday__month=datetime.now().month, 
                                   birthday__day__gte=datetime.now().day).order_by(
            'birthday__day').annotate(day=F('birthday__day') - datetime.now().day)


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    
    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)


class GetEmploymentStatus(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return Response(f"{user.first_name} {user.last_name}") if user.is_active == True \
               else Response({"detail": "Not found."}) 