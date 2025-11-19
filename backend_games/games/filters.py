import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):
    # Rangos numéricos
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    min_year = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    max_year = django_filters.NumberFilter(field_name='year', lookup_expr='lte')

    # Búsqueda parcial en texto
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    developer = django_filters.CharFilter(field_name='developer', lookup_expr='icontains')

    class Meta:
        model = Game
        fields = []  # se definen explícitamente arriba
