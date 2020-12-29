from django_filters import filters, FilterSet
from .models import Expenses
from django.forms.widgets import DateInput


class ExpenseFilter(FilterSet):
    date = filters.DateFilter(widget=DateInput(attrs={'placeholder': 'dd/mm/aaaa', 'type': 'text', 'class': 'datepicker'}))
    class Meta:
        model = Expenses
        fields = ('category', 'long_term', 'currency', 'date')