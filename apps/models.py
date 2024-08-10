from tkinter import CASCADE

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    class UserType(models.TextChoices):
        pr_ow = "personal_owner", "Personal Owner"
        rz = "olib_sotar", "Olib Sotar"

    user_type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.pr_ow
    )
    phone_number = models.CharField(max_length=15, unique=True, )
    balance = models.BigIntegerField(default=0)
    organization = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Favorite(models.Model):
    user_id = models.ForeignKey('User', on_delete=CASCADE)
    listing_id = models.ForeignKey('Listing', on_delete=CASCADE)


class Listing(models.Model):
    class OperationType(models.TextChoices):
        s = "sale", "Sale"
        r = "rent", "Rent"

    class Currency(models.TextChoices):
        uz = 'uzs', 'UZS'
        us = 'usd', 'USD'

    operationType = models.CharField( max_length=2,
        choices=OperationType.choices,
        default=OperationType.s
    )
    userId = models.ForeignKey('User', on_delete=CASCADE)
    categoryId = models.ForeignKey('Category')
    description = models.CharField(120)
    price = models.BigIntegerField
    priceCurrency = models.CharField(
        max_length=2,
        choices=OperationType.choices,
        default=OperationType.s
    )


class Category(models.Model):
    class UserType(models.TextChoices):
        s = "sale", "Sale"
        r = "rent", "Rent"

    operation_types = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.s
    )
    name = models.CharField(255)
    parentId = models.ForeignKey('self')
    isActive = models.BooleanField
    weight = models.SmallIntegerField
    createdAT = models.DateTimeField(auto_now=True)
    updateAT = models.DateTimeField(auto_now=True)
