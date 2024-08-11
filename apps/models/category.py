from django.db import models

from apps.models.base import CustomModel


class Category(CustomModel):
    name = models.CharField(max_length=50)
    parentId = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    isActive = models.BooleanField(db_default=False)
    weight = models.SmallIntegerField(db_default=0)

