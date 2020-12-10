from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from expenses.models import Expenses, Category
from profiles.models import Profile


class ExpensesDashboardView(ListView):
    template_name = 'expenses_dashboard/expenses_dashboard.html'
    model = Expenses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Expenses.objects.filter(author__in=profile)
        currency_list = list(set([i.currency for i in query]))
        category = Category.objects.all()
        context["currency"] = currency_list
        context["categories"] = category
        return context
    

