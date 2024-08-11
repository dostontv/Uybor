from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.models.base import CustomModel


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


class Listing(CustomModel):
    userId = models.ForeignKey('User', on_delete=models.CASCADE)
    categoryId = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    price = models.BigIntegerField()
    priceCurrency = models.CharField(max_length=4, choices=Currency.choices, default=Currency.uz)
    isPriceAuction = models.BooleanField(db_default=False)
    priceType = models.CharField(max_length=4, choices=PriceType.choices, db_default=PriceType.all)
    room = models.SmallIntegerField(db_default=1)
    pricePeriodUnit = models.CharField(max_length=155, null=True)
    square = models.SmallIntegerField(db_default=1)
    floor = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin FloorTotal dan kichik bo'lsin
    floorTotal = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin Floor dan kotaroq bo'lsin
    isNewBuilding = models.BooleanField(db_default=False)
    repair = models.CharField(max_length=20, choices=RepairType.choices)
    foundation = models.CharField(max_length=50)


class ListingImage(models.Model):
    listingId = models.ForeignKey('Listing', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listings/')
