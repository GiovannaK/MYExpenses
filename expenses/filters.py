from django_filters import filters, FilterSet, DateFilter
from .models import Expenses
from django.forms.widgets import DateInput


class ExpenseFilter(FilterSet):
    
    start_date = DateFilter(field_name="date", lookup_expr="gte", widget=DateInput(attrs={
        'placeholder': 'dd/mm/yyyy', 'type': 'text', 'class': 'datepicker'
    }))
    
    end_date = DateFilter(field_name="date", lookup_expr="lte", widget=DateInput(attrs={
        'placeholder': 'dd/mm/yyyy', 'type': 'text', 'class': 'datepicker'
    }))

    class Meta:
        model = Expenses
        fields = ('category', 'long_term', 'currency')