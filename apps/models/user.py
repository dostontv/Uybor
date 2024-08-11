from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        pr_ow = 'Private Owner', 'private owner'
        dev = 'Developer', 'developer'
        realtor = 'Realtor', 'realtor'
        moder = 'Moderator', 'moderator'

    phone_number = models.CharField(max_length=15, unique=True)
    balance = models.BigIntegerField(db_default=0)
    organization = models.CharField(max_length=50)
    user_type = models.CharField(max_length=13, choices=UserType.choices, default=UserType.pr_ow)


class Favorite(models.Model):
    user_id = models.ForeignKey('apps.User', on_delete=models.CASCADE)
    listing_id = models.ForeignKey('apps.Listing', on_delete=models.CASCADE)
