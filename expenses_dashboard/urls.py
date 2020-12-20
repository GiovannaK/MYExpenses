from django.urls import path
from .views import ExpensesDashboardView, ExpensesReportsListView, expense_pdf_view

app_name = "expense_dash"

urlpatterns = [
    path('expenses_dash/', ExpensesDashboardView.as_view(), name="expenses_dash"),
    path('expenses_reports/', ExpensesReportsListView.as_view(), name="expenses_reports"),
    path('expenses_pdf/', expense_pdf_view, name="expense_pdf")
]
