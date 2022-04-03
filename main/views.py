from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response


class TimeAPIView(APIView):
    """
    Return current time as formatted string
    """
    authentication_classes = []
    def get(self, request, format=None):
        time = timezone.now().strftime('%d-%m-%Y %H:%M:%S')
        return Response(time)
