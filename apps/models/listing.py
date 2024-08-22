from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.models.base import CustomModel


class Listing(CustomModel):
    class Currency(models.TextChoices):
        UZ = 'uzs', 'UZS'
        US = 'usd', 'USD'

    class PriceType(models.TextChoices):
        ALL = 'all', 'All'

    class RepairType(models.TextChoices):
        S = "sredniy", "Sredniy"
        K = "kapital", "Kapital"
        E = "evro", "Evro"
        C = "custom", "Custom"

    class FoundationType(models.TextChoices):
        P = "panel", "Panel"
        K = "kirpich", "Kirpich"

    class MSType(models.TextChoices):
        A = "approved", "Approved"
        C = "canceled", "Cancelled"
        P = "pending", "Pending"

    owner = models.ForeignKey('User', models.CASCADE)
    category = models.ForeignKey('Category', models.SET_NULL, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    place = models.CharField(max_length=100, null=True)
    price = models.BigIntegerField()
    price_currency = models.CharField(max_length=4, choices=Currency.choices, db_default=Currency.UZ)
    price_type = models.CharField(max_length=4, choices=PriceType.choices, db_default=PriceType.ALL)
    price_period_unit = models.CharField(max_length=155, null=True)
    room = models.SmallIntegerField(db_default=1)
    is_active = models.BooleanField(db_default=False)
    is_price_auction = models.BooleanField(db_default=False)
    square = models.SmallIntegerField(db_default=1)
    floor = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin FloorTotal dan kichik bo'lsin
    floor_total = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin Floor dan kotaroq bo'lsin
    is_new_building = models.BooleanField(db_default=False)
    repair = models.CharField(max_length=20, choices=RepairType.choices)
    foundation = models.CharField(max_length=15, choices=FoundationType.choices, null=True)
    residential_complex_id = models.BooleanField(null=True)
    moderation_status = models.CharField(max_length=20, choices=MSType.choices, db_default=MSType.P)
    urgently_expired_at = models.DateField(null=True)
    verified_expired_at = models.DateField(null=True)
    premium_expired_at = models.DateField(null=True)
    vip_expired_at = models.DateField(null=True)
    views = models.BigIntegerField(db_default=0)
    favorites = models.SmallIntegerField(db_default=0)
    is_vip = models.BooleanField(db_default=False)
    is_premium = models.BooleanField(db_default=False)
    is_urgently = models.BooleanField(db_default=False)


class ListingImage(models.Model):
    listing = models.ForeignKey('Listing', models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='listings/')
