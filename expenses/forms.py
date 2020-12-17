from django.forms import ModelForm, DateTimeInput
from .models import Expenses
from django.forms import ValidationError


class ExpenseCreationForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'date', 'title', 'quantity', 'currency', 'long_term']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'text', 'class': 'datepicker'})
        }


class ExpenseUpdateForm(ModelForm):        
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'date', 'title', 'quantity', 'currency', 'long_term']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'})
        }

