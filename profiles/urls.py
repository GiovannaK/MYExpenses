from django.urls import path
from .views import ProfileView

app_name = 'profile'

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    #path('update_info/<int:pk>/', ProfileUpdateInfoView.as_view(), name='update_info')
]
