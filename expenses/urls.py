from django.urls import path
from .views import ExpenseListView, HomeTemplateView


app_name = 'expense'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('expenses/', ExpenseListView.as_view(), name="list")
]