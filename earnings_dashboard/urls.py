from django.urls import path
from .views import EarningsDashboardView

app_name="earning_dash"

urlpatterns = [
    path('earnings_dash/', EarningsDashboardView.as_view(), name="earnings_dash")
]
