from django_filters import filters, FilterSet
from .models import Earns
from django.forms.widgets import DateTimeInput


class EarningFilter(FilterSet):
    date = filters.DateFilter(widget=DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa', 'type': 'text', 'class': 'datepicker'}))
    class Meta:
        model = Earns
        fields = ('category', 'long_term', 'currency', 'date')
        