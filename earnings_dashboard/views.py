from django.shortcuts import render
from django.views.generic.list import ListView
from earns.models import Earns, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from .utils.custom_datetime_utils import start_date, end_date, initial_year, final_year, month_end, month_start, initial_three_months, final_three_months
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class EarningsDashboardView(LoginRequiredMixin, ListView):
    template_name = "earnings_dashboard/earnings_dashboard.html"
    model = Earns
    login_url = 'signin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Earns.objects.filter(author__in=profile)

        earnings_per_month = query.filter(date__range=[start_date, end_date]).annotate(month=ExtractMonth('date')).values('month').annotate(sum=Sum('quantity')).order_by()
        earnings_per_week = query.filter(date__range=[month_start, month_end]).annotate(week=ExtractWeek('date')).values('week').annotate(sum=Sum('quantity')).order_by('week')
        earnings_per_category = query.values('category__name').annotate(sum=Sum('quantity')).order_by('category')
        earnings_last_five_years = query.filter(date__range=[initial_year, final_year]).annotate(year=ExtractYear('date')).values('year').annotate(sum=Sum('quantity')).order_by('year')
        
        context["earnings_per_month"] = earnings_per_month
        context["earnings_per_week"] = earnings_per_week
        context["earnings_per_category"] = earnings_per_category
        context["earnings_last_five_years"] = earnings_last_five_years
        return context
    
