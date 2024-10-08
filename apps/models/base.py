from django.db import models


class CustomModel(models.Model):
    class Meta:
        abstract = True

    class OperationType(models.TextChoices):
        S = "sale", "Sale"
        R = "rent", "Rent"

    operation_type = models.CharField(max_length=5, choices=OperationType.choices, db_default=OperationType.R)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
