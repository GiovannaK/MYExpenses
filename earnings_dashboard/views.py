from django.shortcuts import render
from django.views.generic.list import ListView
from earns.models import Earns, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from earnings_dashboard.utils.custom_datetime_utils import start_date, end_date, initial_year, final_year, month_end, month_start, initial_last_year, final_last_year, current_year, last_three_months
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class EarningsDashboardView(LoginRequiredMixin, ListView):
    template_name = "earnings_dashboard/earnings_dashboard.html"
    model = Earns
    login_url = 'account_login'

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
    

class EarningsReportsListView(LoginRequiredMixin, ListView):
    template_name = 'earnings_dashboard/earnings_reports.html'
    model = Earns
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Earns.objects.filter(author__in=profile)
        
        currency_current_moment = query.values('currency__currency').annotate(sum=Sum('quantity')).order_by('currency')
        currency_current_month = currency_current_moment.filter(date__range=[month_start, month_end])
        currency_current_year = currency_current_moment.filter(date__range=[start_date, end_date])
        currency_last_three_months = currency_current_moment.filter(date__gte=last_three_months)
        currency_last_year = currency_current_moment.filter(date__range=[initial_last_year, final_last_year])

        total_current_year = query.filter(date__range=[start_date, end_date]).aggregate(Sum('quantity'))['quantity__sum']
        total_current_month = query.filter(date__range=[month_start, month_end]).aggregate(Sum('quantity'))['quantity__sum']
        total_last_three_months = query.filter(date__gte=last_three_months).aggregate(Sum('quantity'))['quantity__sum']

        context["currency_current_year"] = currency_current_year
        context["currency_current_moment"] = currency_current_moment
        context["currency_current_month"] = currency_current_month
        context["currency_last_three_months"] = currency_last_three_months
        context["currency_last_year"] = currency_last_year
        context["total_current_year"] = total_current_year
        context["total_current_month"] = total_current_month
        context["total_last_three_months"] = total_last_three_months
        return context


login_required(login_url="account_login")    
def earnings_pdf_view(request):
    template_path = 'earnings_dashboard/earnings_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    profile = Profile.objects.filter(user=request.user)
    query = Earns.objects.filter(author__in=profile)
    
    year = current_year

    currency_current_moment = query.values('currency__currency').annotate(sum=Sum('quantity')).order_by('currency')
    currency_current_month = currency_current_moment.filter(date__range=[month_start, month_end])
    currency_current_year = currency_current_moment.filter(date__range=[start_date, end_date])
    currency_last_year = currency_current_moment.filter(date__range=[initial_last_year, final_last_year])
    total_current_year = query.filter(date__range=[start_date, end_date]).aggregate(Sum('quantity'))['quantity__sum']
    total_current_month = query.filter(date__range=[month_start, month_end]).aggregate(Sum('quantity'))['quantity__sum']
    
    context = {
            'currency_current_moment': currency_current_moment,
            'currency_current_month':currency_current_month,
            'currency_current_year': currency_current_year,
            'currency_last_year': currency_last_year,
            'total_current_year': total_current_year,
            'total_current_month': total_current_month,
            'current_year': year,
        }
    
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('404 not found')
    return response          