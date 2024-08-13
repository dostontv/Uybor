from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.models.base import CustomModel


class Listing(CustomModel):
    class Currency(models.TextChoices):
        uz = 'uzs', 'UZS'
        us = 'usd', 'USD'

    class PriceType(models.TextChoices):
        all = 'all', 'All'

    class RepairType(models.TextChoices):
        s = "sredniy", "Sredniy"
        k = "kapital", "Kapital"
        e = "evro", "Evro"
        c = "custom", "Custom"

    class FoundationType(models.TextChoices):
        p = "panel", "Panel"
        k = "kirpich", "Kirpich"

    class MSType(models.TextChoices):
        a = "approved", "Approved"
        c = "canceled", "Cancelled"
        p = "pending", "Pending"

    owner = models.ForeignKey('User', models.CASCADE)
    category = models.ForeignKey('Category', models.SET_NULL, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    place = models.CharField(max_length=100, null=True)
    price = models.BigIntegerField()
    price_currency = models.CharField(max_length=4, choices=Currency.choices, default=Currency.uz)
    price_type = models.CharField(max_length=4, choices=PriceType.choices, db_default=PriceType.all)
    price_periodUnit = models.CharField(max_length=155, null=True)
    room = models.SmallIntegerField(db_default=1)
    is_price_auction = models.BooleanField(db_default=False)
    square = models.SmallIntegerField(db_default=1)
    floor = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin FloorTotal dan kichik bo'lsin
    floor_total = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin Floor dan kotaroq bo'lsin
    is_new_building = models.BooleanField(db_default=False)
    repair = models.CharField(max_length=20, choices=RepairType.choices)
    foundation = models.CharField(max_length=15, choices=FoundationType.choices, null=True)
    residential_complex_id = models.BooleanField(null=True)
    moderation_status = models.CharField(max_length=20, choices=MSType.choices, db_default=MSType.p)
    urgently_expiredAt = models.DateField(null=True)
    verified_expiredAt = models.DateField(null=True)
    premium_expiredAt = models.DateField(null=True)
    vip_expiredAt = models.DateField(null=True)
    views = models.BigIntegerField(db_default=0)
    favorites = models.SmallIntegerField(db_default=0)
    is_vip = models.BooleanField(db_default=False)
    is_premium = models.BooleanField(db_default=False)
    is_urgently = models.BooleanField(db_default=False)


class ListingImage(models.Model):
    listing_id = models.ForeignKey('Listing', models.CASCADE)
    image = models.ImageField(upload_to='listings/')
