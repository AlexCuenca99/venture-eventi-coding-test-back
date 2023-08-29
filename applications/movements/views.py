from rest_framework import generics

from .models import Movement
from .serializers import MovementTypesSerializer


class ReportMovementsTypes(generics.ListAPIView):
    queryset = Movement.objects.filter(id=1).count()
    serializer_class = MovementTypesSerializer()
    