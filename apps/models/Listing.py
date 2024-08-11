from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.models.base import CustomModel


class Listing(CustomModel):
    class Currency(models.TextChoices):
        uz = 'uzs', 'UZS'
        us = 'usd', 'USD'

    class PriceType(models.TextChoices):
        all = 'all', 'All'

    userId = models.ForeignKey('User', on_delete=models.CASCADE)
    categoryId = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    price = models.BigIntegerField()
    priceCurrency = models.CharField(max_length=4, choices=Currency.choices, default=Currency.uz)
    isPriceAuction = models.BooleanField(db_default=False)
    priceType = models.CharField(max_length=4, choices=PriceType.choices, db_default=PriceType.all)


class ListingImage(models.Model):
    listingId = models.ForeignKey('Listing', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listings/')
