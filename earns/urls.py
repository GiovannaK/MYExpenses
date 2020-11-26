from django.urls import path
from .views import EarnsListView, SearchEarns, EarnsCreateView


app_name = 'earn'

urlpatterns = [
    path('myearns/', EarnsListView.as_view(), name="list"),
    path('search/', SearchEarns.as_view(), name="search"),
    path('create_earn/', EarnsCreateView.as_view(), name="create"),
]
