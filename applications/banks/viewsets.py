from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import filters

from .models import Bank
from .serializers import BankModelSerializer


class BankModelViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankModelSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["client"]
