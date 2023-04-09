import operator
from django.db.models.functions import ExtractMonth
from django.db.models import Value
from rest_framework import serializers
from user.models.base import User
from notify.models import *


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def to_representation(self, instance):
        representation = super(HistorySerializer, self).to_representation(instance)
        lateness = list(instance.lateness.values().annotate(month=ExtractMonth('created_datetime'), title=Value(Lateness.__name__)))
        remote = list(instance.remote_set.values().annotate(month=ExtractMonth('created_datetime'), title=Value(Remote.__name__)))
        timeoff = list(instance.timeoff_set.values().annotate(month=ExtractMonth('created_datetime'), title=Value(Timeoff.__name__)))
        history = [*lateness, *remote, *timeoff]
        representation['history'] = sorted(history, key=operator.itemgetter('created_datetime'))[::-1]
        return representation