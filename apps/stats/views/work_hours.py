from datetime import date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, F
from user.models import User
from notify.models.late import Lateness


class WorkHoursView(APIView):
    pass

