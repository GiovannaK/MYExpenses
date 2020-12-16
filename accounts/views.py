from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages


class SignUpView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = UserRegistrationForm

    def form_invalid(self, form):
        messages.error(self.request, 'Verifique se todas as informações estão corretas!')
        return super(SignUpView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Conta criada com sucesso! Faça login para continuar')
        return reverse_lazy('signin')


class loginUserView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, 'Usuário ou senha incorretos!')
        return super(loginUserView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('expense:list')
    
    

