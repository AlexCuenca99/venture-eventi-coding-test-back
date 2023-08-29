from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel

User = get_user_model()


class Bank(TimeStampedModel):
    number = models.CharField("Number", max_length=50, unique=True)
    client = models.CharField("Nombre", max_length=100, unique=True)
    date = models.DateField("Date", default="2023-08-26")

    def __str__(self) -> str:
        return self.number + self.client
