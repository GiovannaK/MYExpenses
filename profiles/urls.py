from django.urls import path
from .views import ProfileView, ProfileUpdateInfoView

app_name = 'profile'

urlpatterns = [
    path('profile/<str:pk>/', ProfileView.as_view(), name='profile'),
    path('update_info/<str:pk>/', ProfileUpdateInfoView.as_view(), name='update_info'),
]
