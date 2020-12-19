from django.urls import path
from .views import ExpensesDashboardView, ExpensesReportsTemplateView

app_name = "expense_dash"

urlpatterns = [
    path('expenses_dash/', ExpensesDashboardView.as_view(), name="expenses_dash"),
    path('expenses_reports/', ExpensesReportsTemplateView.as_view(), name="expenses_reports")
]
