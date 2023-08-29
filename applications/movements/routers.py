from rest_framework import routers

from .viewsets import MovementModelViewSet, MovementTypeModelViewSet


router = routers.DefaultRouter()
router.register(
    r"movements-types", MovementTypeModelViewSet, basename="movements-types"
)
router.register(r"movements", MovementModelViewSet, basename="movements")
