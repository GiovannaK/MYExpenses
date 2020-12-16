from django.urls import path
from .views import ExpenseListView, HomeTemplateView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, SearchExpenses


app_name = 'expense'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('expenses/', ExpenseListView.as_view(), name="list"),
    path('create_expense/', ExpenseCreateView.as_view(), name="create"),
    path('<str:pk>/update_expense/', ExpenseUpdateView.as_view(), name="update"),
    path('delete_expense/<str:pk>/', ExpenseDeleteView.as_view(), name="delete"),
    path('search/', SearchExpenses.as_view(), name="search")
]