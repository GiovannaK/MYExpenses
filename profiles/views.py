from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .models import Profile


class ProfileView(ListView):
    template_name = 'profiles/profile.html'
    context_object_name = 'user'
    
    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)
    
