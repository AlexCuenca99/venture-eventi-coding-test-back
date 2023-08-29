from django.db.models.query import QuerySet
from django.db.models import Count, Sum
from decimal import Decimal
from dataclasses import dataclass

from .models import MovementType, Movement


@dataclass
class MovementReportEntry:
    name: str
    amount: Decimal
    count: int


def movement_report() -> list[MovementReportEntry]:
    """Generate query for get all movement types with the number of transactions and total

    Returns:
        list[MovementReportEntry]: _description_
    """
    data = []

    queryset = (
        MovementType.objects.annotate(count_movement_types=Count("type"))
        .annotate(total_movement_type=Sum("type__value"))
        .order_by("total_movement_type")
    )

    for entry in queryset:
        report_entry = MovementReportEntry(
            name=entry.name,
            amount=entry.total_movement_type if entry.total_movement_type else 0,
            count=entry.count_movement_types,
        )

        data.append(report_entry)

    return data
