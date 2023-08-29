from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import MovementType, Movement
from .serializers import MovementTypeModelSerializer, MovementModelSerializer
from rest_framework import filters


class MovementTypeModelViewSet(viewsets.ModelViewSet):
    queryset = MovementType.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MovementTypeModelSerializer


class MovementModelViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MovementModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["bank"]
