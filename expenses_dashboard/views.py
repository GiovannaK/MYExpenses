from django.shortcuts import render
from django.views.generic import TemplateView


class ExpensesDashboardView(TemplateView):
    template_name = 'expenses_dashboard/expenses_dashboard.html'

