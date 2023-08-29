from django.db import models

from model_utils.models import TimeStampedModel

from applications.banks.models import Bank


class MovementType(TimeStampedModel):
    code = models.CharField("Code", max_length=50, unique=True)
    name = models.CharField("Name", max_length=50, unique=True)
    description = models.CharField("Description", max_length=100)

    def __str__(self) -> str:
        return self.code + " - " + self.name


class Movement(TimeStampedModel):
    mo_type = models.ForeignKey(
        "MovementType", on_delete=models.CASCADE, related_name="type"
    )
    value = models.DecimalField("Valor", max_digits=5, decimal_places=2)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="banks")

    def __str__(self) -> str:
        return self.mo_type.name + " - " + str(self.value) + "$"
