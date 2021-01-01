from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from expenses.models import Expenses, Category
from profiles.models import Profile
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear
from django.contrib.auth.mixins import LoginRequiredMixin
from earnings_dashboard.utils.custom_datetime_utils import start_date, end_date, initial_year, final_year, month_end, month_start, initial_last_year, final_last_year, current_year, last_three_months
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

class ExpensesDashboardView(LoginRequiredMixin, ListView):
    template_name = 'expenses_dashboard/expenses_dashboard.html'
    model = Expenses
    login_url = 'account_login'

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


class ExpensesReportsListView(LoginRequiredMixin, ListView):
    template_name = 'expenses_dashboard/expenses_reports.html'
    model = Expenses
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user)
        query = Expenses.objects.filter(author__in=profile)
        
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


@login_required(login_url="account_login")    
def expense_pdf_view(request):
    template_path = 'expenses_dashboard/expenses_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    profile = Profile.objects.filter(user=request.user)
    query = Expenses.objects.filter(author__in=profile)
    
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

        


    