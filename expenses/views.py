from django.shortcuts import render
from .models import Category, Expenses, Currencies
from profiles.models import Profile
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from .forms import ExpenseCreationForm
import os
import json


class HomeTemplateView(TemplateView):
    template_name = 'expenses/landing_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        validate_create_currency = Currencies.objects.all().exists()
        if validate_create_currency == False:
            with open(os.path.join(settings.BASE_DIR, 'currency.json'), 'r', 
            encoding="utf8") as data:
                data_json = json.loads(data.read())
                for v in data_json.values():
                    symbol = v["symbol"]
                    create_currency = Currencies.objects.create(currency=symbol)
        get_currency = Currencies.objects.all()
        context["currencies"] = get_currency
        return context 


class ExpenseListView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expenses.objects.filter(author__in=profile)
        return context
    

class ExpenseCreateView(CreateView):
    model = Expenses
    template_name = 'expenses/add_expense.html'
    form_class = ExpenseCreationForm
    
    def form_valid(self, form):
        title_input = form.cleaned_data.get('title')
        instance = form.save(commit=False)
        instance.author = Profile.objects.get(user=self.request.user)
        instance.currency = form.cleaned_data.get('currency')
        instance.category = form.cleaned_data.get('category')
        instance.save()
        messages.success(self.request, f'{title_input} foi criado com sucesso!')
        return super(ExpenseCreateView, self).form_valid(form)

    def form_invalid(self, form):
        self.form_class    
        return super(ExpenseCreateView, self).form_invalid(form)    
    
    def get_success_url(self):
        return reverse('expense:create')
    
