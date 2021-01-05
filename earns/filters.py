from django_filters import filters, FilterSet, DateFilter
from .models import Earns
from django.forms.widgets import DateInput


class EarningFilter(FilterSet):
    
    start_date = DateFilter(field_name="date", lookup_expr="gte", widget=DateInput(attrs={
        'placeholder': 'dd/mm/yyyy', 'type': 'text', 'class': 'datepicker'
    }))
    
    end_date = DateFilter(field_name="date", lookup_expr="lte", widget=DateInput(attrs={
        'placeholder': 'dd/mm/yyyy', 'type': 'text', 'class': 'datepicker'
    }))

    class Meta:
        model = Earns
        fields = ('category', 'long_term', 'currency')
        