from django.urls import path
from .views import EarnsListView, SearchEarns, EarnsCreateView, EarnsUpdateView, EarnDeleteView


app_name = 'earn'

urlpatterns = [
    path('myearns/', EarnsListView.as_view(), name="list"),
    path('search/', SearchEarns.as_view(), name="search"),
    path('create_earn/', EarnsCreateView.as_view(), name="create"),
    path('<int:pk>/update_earn/', EarnsUpdateView.as_view(), name="update"),
    path('<int:pk>/delete_earn/', EarnDeleteView.as_view(), name="delete"),
]
