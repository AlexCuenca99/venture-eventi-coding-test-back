from django.urls import path

from .views import MovementTypesReportListView, MovementsIntervalReportListView

urlpatterns = [
    # Charts
    path(
        "reports/movement-types/",
        MovementTypesReportListView.as_view(),
        name="movement-types-report",
    ),
    path(
        "reports/movements-interval/",
        MovementsIntervalReportListView.as_view(),
        name="movements-interval-report",
    ),
]
