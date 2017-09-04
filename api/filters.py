from django_filters import rest_framework as filters
from api.models import Movement
import django_filters


class MovementFilter(filters.FilterSet):
    device = django_filters.CharFilter(name='movement_destination__device')

    class Meta:
        model = Movement
        fields = ['device']
