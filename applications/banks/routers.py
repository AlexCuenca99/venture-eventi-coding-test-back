from rest_framework import routers

from .viewsets import BankModelViewSet


router = routers.DefaultRouter()
router.register(r"banks", BankModelViewSet, basename="banks")
