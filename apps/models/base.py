from django.db import models


class CustomModel(models.Model):
    class Meta:
        abstract = True

    class OperationType(models.TextChoices):
        s = "sale", "Sale"
        r = "rent", "Rent"

    operationType = models.CharField(max_length=5, choices=OperationType.choices, default=OperationType.s)
    createdAT = models.DateTimeField(auto_now=True)
    updateAT = models.DateTimeField(auto_now=True)
