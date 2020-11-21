from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages

class SignUpView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = UserRegistrationForm


    def get_success_url(self):
        messages.success(self.request, 'Conta criada com sucesso! Faça login para continuar')
        return reverse_lazy('accounts:signup')

