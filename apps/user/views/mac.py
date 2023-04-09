# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import OfficeHours

# Python
from datetime import datetime

class MacAPIView(APIView):

    def post(self, request):
        user = request.user
        queryset = user.hardware.filter(mac_address__in=request.data)
        if user.work_type.work_type != 'Remote':
            if queryset.exists():
                if user.work_type.work_type != 'At office': 
                    user.work_type.work_type = 'At office'
                    user.work_type.save()
            else:
                if user.work_type.work_type != 'Absent':
                    user.work_type.work_type = 'Absent'
                    hours = datetime.now().hour - user.work_type.modified_datetime.hour
                    minutes = datetime.now().minute - user.work_type.modified_datetime.minute
                    OfficeHours.objects.create(user=user, hours=hours, minutes=minutes)
                    user.work_type.save()
            user.save()
        return Response({'response': 'Request sent'}, status=200)