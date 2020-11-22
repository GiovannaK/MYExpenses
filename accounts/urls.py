from django.urls import path
from .views import SignUpView, loginUserView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signin/', loginUserView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
