from django.shortcuts import render
from django.views.generic.list import ListView
from earns.models import Earns, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from datetime import datetime
# Create your views here.


class EarningsDashboardView(ListView):
    template_name = "earnings_dashboard/earnings_dashboard.html"
    model = Earns

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Earns.objects.filter(author__in=profile)

        current_year = datetime.now().year
        current_month = datetime.now().month
        five_years_ago = current_year - 5

        month_start = datetime(year=current_year, month=current_month, day=1)
        month_end = datetime(year=current_year, month=current_month, day=31)

        start_date = datetime(year=current_year, month=1, day=1)
        end_date = datetime(year=current_year, month=12, day=31)

        initial_year = datetime(year=five_years_ago, month=1, day=1)
        final_year = datetime(year=current_year, month=12, day=31)

        earnings_per_month = query.filter(date__range=[start_date, end_date]).annotate(month=ExtractMonth('date')).values('month').annotate(sum=Sum('quantity')).order_by()
        earnings_per_week = query.filter(date__range=[month_start, month_end]).annotate(week=ExtractWeek('date')).values('week').annotate(sum=Sum('quantity')).order_by('week')
        earnings_per_category = query.values('category').annotate(sum=Sum('quantity')).order_by('category')
        earnings_last_five_years = query.filter(date__range=[initial_year, final_year]).annotate(year=ExtractYear('date')).values('year').annotate(sum=Sum('quantity')).order_by('year')
        
        context["earnings_per_month"] = earnings_per_month
        context["earnings_per_week"] = earnings_per_week
        context["categories"] = Category.objects.all().order_by('id')
        context["earnings_per_category"] = earnings_per_category
        context["earnings_last_five_years"] = earnings_last_five_years
        return context
    
