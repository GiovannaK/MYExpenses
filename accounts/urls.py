from django.urls import path
from .views import SignUpView, loginUserView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signin/', loginUserView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_reset/', 
    auth_views.PasswordResetView.as_view(
        template_name="accounts/update_password.html"),
        name="password_reset"),
    
    path('password_reset_done/', 
    auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"), 
        name="password_reset_done"),
    
    path('password_reset_confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html"),
        name="password_reset_confirm"),
    
    path('password_reset_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), 
    name="password_reset_complete"),
]
