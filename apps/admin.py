from django.contrib import admin
from django.contrib.admin import StackedInline

from apps.models import Listing, ListingImage


class ListingImageStackedInline(StackedInline):
    model = ListingImage
    min_num = 0
    max_num = 20
    extra = 0


@admin.register(Listing)
class ListingModelAdmin(admin.ModelAdmin):
    inlines = [ListingImageStackedInline]
