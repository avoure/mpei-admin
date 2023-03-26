from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
