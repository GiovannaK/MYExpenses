import django_filters
from .models import Earns

class EarningFilter(django_filters.FilterSet):
    class Meta:
        model = Earns
        fields = ('category', 'long_term', 'currency', 'date')