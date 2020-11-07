from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Expenses

class ExpenseCreationForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'date', 'title', 'quantity', 'currency']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'})
        }