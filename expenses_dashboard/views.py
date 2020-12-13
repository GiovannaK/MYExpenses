from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from expenses.models import Expenses, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek
from datetime import datetime, timedelta


class ExpensesDashboardView(ListView):
    template_name = 'expenses_dashboard/expenses_dashboard.html'
    model = Expenses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Expenses.objects.filter(author__in=profile)
        #currency_list = list(set([i.currency for i in query]))

        current_year = datetime.now().year
        current_month = datetime.now().month
        start_date = datetime(year=current_year, month=1, day=1)
        end_date = datetime(year=current_year, month=12, day=31)

        expenses_each_month = query.filter(date__range=[start_date, end_date]).annotate(month=ExtractMonth('date')).values('month').annotate(sum=Sum('quantity')).order_by()
        expenses_per_week = query.filter(date__month=current_month).annotate(week=ExtractWeek('date')).values('week').annotate(sum=Sum('quantity')).order_by('week')
        
        category = Category.objects.all()
        #context["currency"] = currency_list
        context["categories"] = category
        context["expenses_each_month"] = expenses_each_month
        context["expenses_per_week"] = expenses_per_week
        return context
    

