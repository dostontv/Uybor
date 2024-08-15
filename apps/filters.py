from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import F
from django_filters import rest_framework as filters

from apps.models import Listing


class ListingFilter(filters.FilterSet):
    search = filters.CharFilter(method='search_filter')
    data = filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Listing
        fields = ['search', 'data']

    def search_filter(self, queryset, name, value):
        if value and value != 'sale':
            return queryset.annotate(similarity=TrigramSimilarity(F('place'), value)).filter(
                similarity__gt=0.1,
                is_active=True
            )
        return queryset.filter(is_active=True, moderation_status=Listing.MSType.a)
