from django_filters import rest_framework as filters
from .models import Table


class TableFilters(filters.FilterSet):
    title_exact = filters.CharFilter(field_name='title', lookup_expr='exact')
    title_is = filters.CharFilter(field_name='title', lookup_expr='contains')
    count_gt = filters.NumberFilter(field_name='count', lookup_expr=('gt'))
    count_lt = filters.NumberFilter(field_name='count', lookup_expr=('lt'))
    count_exact = filters.NumberFilter(field_name='count', lookup_expr=('exact'))
    distance_gt = filters.NumberFilter(field_name='distance', lookup_expr=('gt'))
    distance_lt = filters.NumberFilter(field_name='distance', lookup_expr=('lt'))
    distance_exact = filters.NumberFilter(field_name='distance', lookup_expr=('exact'))

    class Meta:
        model = Table
        fields = ('title', 'count', 'distance')