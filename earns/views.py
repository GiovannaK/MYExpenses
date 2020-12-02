from django.shortcuts import render
from .models import Category, Earns
from profiles.models import Profile
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EarnsCreationForm, EarnsUpdateForm


class EarnsListView(LoginRequiredMixin, ListView):
    model = Earns
    template_name = 'earns/earnings.html'
    context_object_name = 'earns'
    paginate_by = 9
    login_url = 'signin'

    def get_queryset(self):
        profile = Profile.objects.filter(user=self.request.user)
        return Earns.objects.filter(author__in=profile) 
    

class SearchEarns(EarnsListView):
    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get('q') or self.request.session['q'] 
        qs = super().get_queryset(*args, **kwargs)

        if not q:
            return qs

        self.request.session['q'] = q

        qs = qs.filter(
            Q(title__icontains=q)|
            Q(description__icontains=q)|
            Q(quantity__icontains=q)|
            Q(date__icontains=q)
        )
        
        self.request.session.save()

        return qs   


class EarnsCreateView(LoginRequiredMixin, CreateView):
    model = Earns
    template_name = 'earns/add_earning.html'
    form_class = EarnsCreationForm
    login_url = 'signin'
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        title_input = form.cleaned_data.get('title')
        title_exists = Earns.objects.filter(author=profile, title=title_input).count()
        if title_exists == 0:
            instance = form.save(commit=False)
            instance.author = profile
            instance.currency = form.cleaned_data.get('currency')
            instance.category = form.cleaned_data.get('category')
            instance.save()
            messages.success(self.request, f'{title_input} foi criado com sucesso!')
            return super(EarnsCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'Este título já existe!')
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse('earn:create')


class EarnsUpdateView(LoginRequiredMixin, UpdateView):
    model = Earns
    template_name = 'earns/update_earning.html'
    form_class = EarnsUpdateForm
    login_url = 'signin'

    def form_valid(self, form):
        title_input = form.cleaned_data.get('title')
        instance = form.save(commit=False)
        instance.author = Profile.objects.get(user=self.request.user)
        instance.currency = form.cleaned_data.get('currency')
        instance.category = form.cleaned_data.get('category')
        instance.save()
        messages.success(self.request, f'{title_input} foi atualizado com sucesso!')
        return super(EarnsUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        self.form_class    
        return super(EarnsUpdateView, self).form_invalid(form)    

    def get_success_url(self):
        return reverse('earn:list')


class EarnDeleteView(LoginRequiredMixin, DeleteView):
    model = Earns
    template_name = 'earns/delete_earn.html'
    login_url = 'signin'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)    
        queryset = Earns.objects.filter(author=profile, pk=self.kwargs['pk'])
        return queryset
    
    def get_success_url(self):
        messages.success(self.request, f'"{self.object.title}" foi excluído com sucesso!')
        return reverse('earn:list')