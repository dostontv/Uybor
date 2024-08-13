from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        pr_ow = 'private owner', 'Private Owner'
        dev = 'developer', 'Developer'
        realtor = 'realtor', 'Realtor'
        moder = 'moderator', 'Moderator'

    password = None
    username = None
    email = None
    phone_number = models.CharField(max_length=15, unique=True)
    balance = models.BigIntegerField(db_default=0)
    organization = models.CharField(max_length=50)
    type = models.CharField(max_length=13, choices=UserType.choices, default=UserType.pr_ow)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []


class Favorite(models.Model):
    user = models.ForeignKey('apps.User', models.CASCADE)
    listing = models.ForeignKey('apps.Listing', models.CASCADE)
