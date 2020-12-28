from django.forms import ModelForm, DateInput
from .models import Expenses
from django.forms import ValidationError


class ExpenseCreationForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'date', 'title', 'quantity', 'currency', 'long_term']
        widgets = {
            'date': DateInput(attrs={'type': 'text', 'class': 'datepicker'})
        }


class ExpenseUpdateForm(ModelForm):        
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'date', 'title', 'quantity', 'currency', 'long_term']
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class': 'datepicker'})
        }

