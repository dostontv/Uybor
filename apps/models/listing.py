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


class MSType(models.TextChoices):
    a = "approved", "Approved"
    c = "canceled", "Cancelled"
    p = "pending", "Pending"


class Listing(CustomModel):
    userId = models.ForeignKey('User', on_delete=models.CASCADE)
    categoryId = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    place = models.CharField(max_length=100, null=True)
    price = models.BigIntegerField()
    priceCurrency = models.CharField(max_length=4, choices=Currency.choices, default=Currency.uz)
    priceType = models.CharField(max_length=4, choices=PriceType.choices, db_default=PriceType.all)
    pricePeriodUnit = models.CharField(max_length=155, null=True)
    room = models.SmallIntegerField(db_default=1)
    isPriceAuction = models.BooleanField(db_default=False)
    square = models.SmallIntegerField(db_default=1)
    floor = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin FloorTotal dan kichik bo'lsin
    floorTotal = models.SmallIntegerField(db_default=1)  # TODO validator yozilsin Floor dan kotaroq bo'lsin
    isNewBuilding = models.BooleanField(db_default=False)
    repair = models.CharField(max_length=20, choices=RepairType.choices)
    foundation = models.CharField(max_length=15, choices=FoundationType.choices, null=True)
    residentialComplexId = models.BooleanField(null=True)
    moderationStatus = models.CharField(max_length=20, choices=MSType.choices, db_default=MSType.p)
    urgentlyExpiredAt = models.DateField(null=True)
    verifiedExpiredAt = models.DateField(null=True)
    premiumExpiredAt = models.DateField(null=True)
    vipExpiredAt = models.DateField(null=True)
    views = models.BigIntegerField(db_default=0)
    favorites = models.SmallIntegerField(db_default=0)
    isVip = models.BooleanField(db_default=False)
    isPremium = models.BooleanField(db_default=False)
    isUrgently = models.BooleanField(db_default=False)


class ListingImage(models.Model):
    listingId = models.ForeignKey('Listing', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listings/')
