from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from expenses.models import Expenses, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from django.contrib.auth.mixins import LoginRequiredMixin
from earnings_dashboard.utils.custom_datetime_utils import start_date, end_date, initial_year, final_year, month_end, month_start


class ExpensesDashboardView(LoginRequiredMixin, ListView):
    template_name = 'expenses_dashboard/expenses_dashboard.html'
    model = Expenses
    login_url = 'signin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Expenses.objects.filter(author__in=profile)

        expenses_each_month = query.filter(date__range=[start_date, end_date]).annotate(month=ExtractMonth('date')).values('month').annotate(sum=Sum('quantity')).order_by()
        expenses_per_week = query.filter(date__range=[month_start, month_end]).annotate(week=ExtractWeek('date')).values('week').annotate(sum=Sum('quantity')).order_by('week')
        expenses_last_five_years = query.filter(date__range=[initial_year, final_year]).annotate(year=ExtractYear('date')).values('year').annotate(sum=Sum('quantity')).order_by('year')      
        expenses_by_category = query.values('category__name').annotate(sum=Sum('quantity')).order_by('category')

        context["expenses_each_month"] = expenses_each_month
        context["expenses_per_week"] = expenses_per_week
        context["expenses_last_five_years"] = expenses_last_five_years
        context["expenses_by_category"] = expenses_by_category
        return context
    

