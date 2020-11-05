from django.shortcuts import render
from .models import Category, Expenses
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class HomeTemplateView(TemplateView):
    template_name = 'expenses/landing_page.html'


class ExpenseListView(ListView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expenses.objects.all() 
        return context
    
    
    
    """ context_object_name = 'expenses'
    queryset = Expenses.objects.all() """