from django.forms import ModelForm, DateTimeInput
from .models import Expenses
from django.forms import ValidationError


class ExpenseCreationForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'date', 'title', 'quantity', 'currency']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'})
        }


    def clean_title(self):
        super(ExpenseCreationForm, self).clean()
        title_cleaned = self.cleaned_data.get('title')
        
        title_bd = Expenses.objects.filter(title__icontains=title_cleaned).exists()

        if title_bd:
            raise ValidationError('Este título já existe!')

        return title_cleaned    


        


