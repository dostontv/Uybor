from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    pass


class Listing(models.Model):
    pass


class Category(models.Model):
    pass
