from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import F, TextChoices
from django_filters import rest_framework as filters

from apps.models import Listing


class ListingFilter(filters.FilterSet):
    class DateType(TextChoices):
        c = "created_at", 'eng esklari boyicha'
        c_ = "-created_at", 'eng yangilari boyicha'

    class expType(TextChoices):
        p = "priceEquivalent", 'eng arzonlari'
        p_ = "-priceEquivalent", 'eng QIMMATLARI'

    class popularType(TextChoices):
        p = "views", 'eng kam korilganlar'
        p_ = "-views", 'eng kop korilganlar'

    class operationType(TextChoices):
        s = "sale", 'Sale'
        r = "rent", 'Rent'

    search = filters.CharFilter(method='search_filter')
    date = filters.ChoiceFilter(method='created_filter', choices=DateType.choices)
    price = filters.ChoiceFilter(method='exp_filter', choices=expType.choices)
    views = filters.ChoiceFilter(method='popular_filter', choices=popularType.choices)
    price__gte = filters.CharFilter(method='price_gte')
    price__lte = filters.CharFilter(method='price_lte')
    operation = filters.ChoiceFilter(method='opertaion_type', choices=operationType.choices)

    class Meta:
        model = Listing
        fields = ['search', 'date', 'price', 'views', 'price__gte', 'price__lte']

    def search_filter(self, queryset, name, value):
        if value and value != 'sale':
            return queryset.annotate(similarity=TrigramSimilarity(F('place'), value)).filter(
                similarity__gt=0.1,
                is_active=True
            )
        return queryset.filter(is_active=True, moderation_status=Listing.MSType.a)

    def created_filter(self, queryset, name, value: str):
        return queryset.filter(is_active=True, moderation_status=Listing.MSType.a).order_by(value)

    def exp_filter(self, queryset, name, value: str):
        if value.startswith('-'):
            return queryset.filter(is_active=True, moderation_status=Listing.MSType.a).order_by('-price')

        return queryset.filter(is_active=True, moderation_status=Listing.MSType.a).order_by('price')

    def popular_filter(self, queryset, name, value: str):
        if value.startswith('-'):
            return queryset.filter(is_active=True, moderation_status=Listing.MSType.a).order_by('-views')

        return queryset.order_by('views')

    def price_gte(self, queryset, name, value: str):
        return queryset.filter(price__gte=int(value))

    def price_lte(self, queryset, name, value: str):
        return queryset.filter(price__lte=int(value))

    def opertaion_type(self, queryset, name, value: str):
        if value.startswith('r'):
            return queryset.filter(operation_type='rent')
        return queryset.filter(operation_type='sale')
