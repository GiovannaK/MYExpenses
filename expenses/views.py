from django.shortcuts import render
from .models import Category, Expenses, Currencies
from profiles.models import Profile
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.conf import settings
from django.urls import reverse
from .forms import ExpenseCreationForm
from .utils import CurrencyCreationObjectMixin
import os
import json



class HomeTemplateView(TemplateView):
    template_name = 'expenses/landing_page.html'


class ExpenseListView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expenses.objects.filter(author__in=profile)
        return context
    

class ExpenseCreateView(CreateView, CurrencyCreationObjectMixin):
    model = Expenses
    template_name = 'expenses/add_expense.html'
    form_class = ExpenseCreationForm
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = Profile.objects.get(user=self.request.user)
        instance.save()
        return super(ExpenseCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('expense:list')
    
