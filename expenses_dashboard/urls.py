from django.urls import path
from .views import ExpensesDashboardView

app_name = "expense_dash"

urlpatterns = [
    path('expenses_dash/', ExpensesDashboardView.as_view(), name="expenses_dash")
]
