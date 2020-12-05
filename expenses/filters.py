from django_filters import filters, FilterSet
from .models import Expenses
from django.forms.widgets import DateTimeInput


class ExpenseFilter(FilterSet):
    date = filters.DateFilter(widget=DateTimeInput(attrs={'placeholder': 'dd/mm/aaaa'}))
    class Meta:
        model = Expenses
        fields = ('category', 'long_term', 'currency', 'date')