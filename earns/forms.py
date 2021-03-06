from django.forms import ModelForm, DateInput
from .models import Earns
from profiles.models import Profile
from django.contrib.auth.models import User
from django.forms import ValidationError

class EarnsCreationForm(ModelForm):    
    class Meta:
        model = Earns
        fields = ['title', 'category', 'description', 'date', 'quantity', 'currency', 'long_term']
        widgets = {
            'date': DateInput(attrs={'type': 'text', 'class': 'datepicker'})
        }


class EarnsUpdateForm(ModelForm):
    class Meta:
        model = Earns
        fields = ['category', 'title', 'description', 'date', 'quantity', 'currency', 'long_term']
        widgets = {
            'date': DateInput(attrs={'type': 'text', 'class': 'datepicker'})
        }