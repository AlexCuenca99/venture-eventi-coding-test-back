from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MovementTypesReportSerializer
from applications.movements.serializers import MovementModelSerializer
from applications.movements.reports import movement_report
from applications.movements.models import Movement


class MovementTypesReportListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MovementTypesReportSerializer

    def get(self, request, *args, **kwargs):
        data = movement_report()
        serializer = self.get_serializer(instance=data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovementsIntervalReportListView(generics.ListAPIView):
    queryset = Movement.objects.all().order_by("value")
    permission_classes = [AllowAny]
    serializer_class = MovementModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "value": [
            "gte",
            "lte",
        ],
    }
