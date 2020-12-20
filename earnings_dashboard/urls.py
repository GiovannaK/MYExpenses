from django.urls import path
from .views import EarningsDashboardView, EarningsReportsListView, earnings_pdf_view

app_name="earning_dash"

urlpatterns = [
    path('earnings_dash/', EarningsDashboardView.as_view(), name="earnings_dash"),
    path('earnings_reports/', EarningsReportsListView.as_view(), name="earnings_reports"),
    path('earnings_pdf/', earnings_pdf_view, name="earnings_pdf"),
]
