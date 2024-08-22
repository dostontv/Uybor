from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    class UserType(models.TextChoices):
        PR_OW = 'private owner', 'Private Owner'
        DEV = 'developer', 'Developer'
        REALTOR = 'realtor', 'Realtor'
        MODER = 'moderator', 'Moderator'

    username = None
    email = None
    phone_number = models.CharField(max_length=15, unique=True)
    balance = models.BigIntegerField(db_default=0)
    organization = models.CharField(max_length=50)
    type = models.CharField(max_length=13, choices=UserType.choices, db_default=UserType.PR_OW)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


class Favorite(models.Model):
    user = models.ForeignKey('apps.User', models.CASCADE)
    listing = models.ForeignKey('apps.Listing', models.CASCADE)
