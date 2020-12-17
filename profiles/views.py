from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ProfileForm, UpdateUserInfo
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/profile.html'
    model = Profile
    form_class = ProfileForm
    login_url = 'signin'
    
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

    def form_invalid(self, form):
        self.form_class    
        messages.error(self.request, 'Verifique se todos os campos foram preenchidos')
        return super(ProfileView, self).form_invalid(form)        

    def get_success_url(self):
        return reverse_lazy('profile:profile', kwargs={'pk': self.request.user.profile.pk})


class ProfileUpdateInfoView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profiles/update_user_info.html'    
    form_class = UpdateUserInfo
    login_url = 'signin'
    
    def form_valid(self, form):
       instance = form.save(commit=False)
       instance.user = self.request.user
       instance.save()
       messages.success(self.request, 'Alterações salvas com sucesso!')
       return super(ProfileUpdateInfoView, self).form_valid(form)        
    
    def form_invalid(self, form):
        self.form_class    
        messages.error(self.request, 'Usuário ou e-mail já existem')
        return super(ProfileUpdateInfoView, self).form_invalid(form)    

    def get_success_url(self):
        return reverse_lazy('profile:profile', kwargs={'pk': self.request.user.profile.pk})
    