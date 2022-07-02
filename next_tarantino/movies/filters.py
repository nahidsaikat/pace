import django_filters

from .models import Movie


class MovieFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['name', 'genre']
