from django_filters import rest_framework as filters
from .models import Place, Animal


class KPfilter(filters.FilterSet):
    object_name = filters.CharFilter(field_name='name', lookup_expr='contains')
    schema_name = filters.CharFilter(field_name='kind', lookup_expr='gte')

    class Meta:
        model = Animal
        fields = ['name', 'kind', 'place']