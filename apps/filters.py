from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import F, TextChoices
from django_filters import rest_framework as filters

from apps.models import Listing


class ListingFilter(filters.FilterSet):
    class DateType(TextChoices):
        C = "created_at", 'eng esklari boyicha'
        C_ = "-created_at", 'eng yangilari boyicha'

    class ExpType(TextChoices):
        P = "priceEquivalent", 'eng arzonlari'
        P_ = "-priceEquivalent", 'eng QIMMATLARI'

    class PopularType(TextChoices):
        P = "views", 'eng kam korilganlar'
        P_ = "-views", 'eng kop korilganlar'

    class OperationType(TextChoices):
        S = "sale", 'Sale'
        R = "rent", 'Rent'

    # search = filters.CharFilter(method='search_filter')
    date = filters.ChoiceFilter(method='created_filter', choices=DateType.choices)
    price = filters.ChoiceFilter(method='exp_filter', choices=ExpType.choices)
    views = filters.ChoiceFilter(method='popular_filter', choices=PopularType.choices)
    price__gte = filters.CharFilter(field_name='price', lookup_expr='gte')
    price__lte = filters.CharFilter(field_name='price', lookup_expr='lte')
    operation = filters.ChoiceFilter(method='opertaion_type', choices=OperationType.choices)

    class Meta:
        model = Listing
        fields = ['date', 'price', 'views', 'price__gte', 'price__lte']

    # def search_filter(self, queryset, name, value):
    #     if value:
    #         return queryset.annotate(similarity=TrigramSimilarity(F('place'), value)).filter(
    #             similarity__gt=0.1,
    #             is_active=True
    #         )
    #     return queryset

    def created_filter(self, queryset, name, value: str):
        if value == '-created_at':
            return queryset.order_by(value)
        return queryset.order_by('created_at')

    def exp_filter(self, queryset, name, value: str):
        if value == '-price':
            return queryset.order_by(value)
        return queryset.order_by('price')

    def popular_filter(self, queryset, name, value: str):
        if value == '-views':
            return queryset.order_by(value)
        return queryset.order_by('views')

    def opertaion_type(self, queryset, name, value: str):
        if value == 'rent':
            return queryset.filter(operation_type=value)
        elif value == 'sale':
            return queryset.filter(operation_type='sale')
