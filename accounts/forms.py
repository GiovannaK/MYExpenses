from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email_form = self.cleaned_data.get("email")
        email_db = User.objects.filter(email=email_form).exists()

        if email_db:
            raise forms.ValidationError('Este E-mail já existe!')
        return email_form





        