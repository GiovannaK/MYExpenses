from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from expenses.models import Expenses, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from datetime import datetime, timedelta


class ExpensesDashboardView(ListView):
    template_name = 'expenses_dashboard/expenses_dashboard.html'
    model = Expenses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Expenses.objects.filter(author__in=profile)

        current_year = datetime.now().year
        current_month = datetime.now().month
        five_years_ago = current_year - 5

        month_start = datetime(year=current_year, month=current_month, day=1)
        month_end = datetime(year=current_year, month=current_month, day=31)

        start_date = datetime(year=current_year, month=1, day=1)
        end_date = datetime(year=current_year, month=12, day=31)

        initial_year = datetime(year=five_years_ago, month=1, day=1)
        final_year = datetime(year=current_year, month=12, day=31)

        expenses_each_month = query.filter(date__range=[start_date, end_date]).annotate(month=ExtractMonth('date')).values('month').annotate(sum=Sum('quantity')).order_by()
        expenses_per_week = query.filter(date__range=[month_start, month_end]).annotate(week=ExtractWeek('date')).values('week').annotate(sum=Sum('quantity')).order_by('week')
        expenses_last_five_years = query.filter(date__range=[initial_year, final_year]).annotate(year=ExtractYear('date')).values('year').annotate(sum=Sum('quantity')).order_by('year')      
        expenses_by_category = query.values('category').annotate(sum=Sum('quantity')).order_by('category')

        category = Category.objects.all().order_by('id')
        context["categories"] = category
        context["expenses_each_month"] = expenses_each_month
        context["expenses_per_week"] = expenses_per_week
        context["expenses_last_five_years"] = expenses_last_five_years
        context["expenses_by_category"] = expenses_by_category
        return context
    

