from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile


class ProfileView(UpdateView):
    template_name = 'profiles/profile.html'
    model = Profile
    form_class = ProfileForm
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        messages.success(self.request, 'Alterações salvas com sucesso!')
        return super(ProfileView, self).form_valid(form)    

    def get_success_url(self):
        profile_id = self.kwargs['pk']
        return reverse_lazy('profile:profile', kwargs={'pk': profile_id})


    