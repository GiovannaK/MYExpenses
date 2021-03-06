from django.shortcuts import render
from .models import Category, Expenses, Currencies
from profiles.models import Profile
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.urls import reverse, reverse_lazy
from .forms import ExpenseCreationForm, ExpenseUpdateForm
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ExpenseFilter
import os
import json


class HomeTemplateView(TemplateView):
    template_name = 'expenses/landing_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        validate_create_currency = Currencies.objects.all().exists()
        if validate_create_currency == False:
            with open(os.path.join(settings.BASE_DIR, 'currency.json'), 'r', 
            encoding="utf8") as data:
                data_json = json.loads(data.read())
                for v in data_json.values():
                    symbol = v["symbol"]
                    create_currency = Currencies.objects.create(currency=symbol)
        get_currency = Currencies.objects.all()
        context["currencies"] = get_currency
        return context 


class ExpenseListView(LoginRequiredMixin, FilterView):
    model = Expenses
    template_name = 'expenses/expenses.html'
    paginate_by = 6
    context_object_name = 'expenses'
    login_url = 'account_login'
    filterset_class = ExpenseFilter

    def get_queryset(self):
        profile = Profile.objects.filter(user=self.request.user)
        return Expenses.objects.filter(author__in=profile)
    

class SearchExpenses(ExpenseListView):
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


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expenses
    template_name = 'expenses/add_expense.html'
    form_class = ExpenseCreationForm
    login_url = 'account_login'
    
    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        title_input = form.cleaned_data.get('title')
        title_exists = Expenses.objects.filter(author=profile, title=title_input).count()
        if title_exists == 0:
            instance = form.save(commit=False)
            instance.author = profile
            instance.currency = form.cleaned_data.get('currency')
            instance.category = form.cleaned_data.get('category')
            instance.save()           
            messages.success(self.request, f'{title_input} foi criado com sucesso!')
            return super(ExpenseCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'Este título já existe!')
            return self.form_invalid(form)    

    def form_invalid(self, form):
        self.form_class    
        return super(ExpenseCreateView, self).form_invalid(form)    
    
    def get_success_url(self):
        return reverse('expense:create')
    

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expenses
    template_name = 'expenses/update_expense.html'
    form_class = ExpenseUpdateForm
    login_url = 'account_login'

    def form_valid(self, form):
        title_input = form.cleaned_data.get('title')
        instance = form.save(commit=False)
        instance.author = Profile.objects.get(user=self.request.user)
        instance.currency = form.cleaned_data.get('currency')
        instance.category = form.cleaned_data.get('category')
        instance.save()
        messages.success(self.request, f'{title_input} foi atualizado com sucesso!')
        return super(ExpenseUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        self.form_class    
        return super(ExpenseUpdateView, self).form_invalid(form)    

    def get_success_url(self):
        return reverse('expense:list')


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expenses    
    template_name = 'expenses/delete_expense.html'
    login_url = 'account_login'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        queryset = Expenses.objects.filter(author=profile, pk=self.kwargs['pk'])
        return queryset
    
    def get_success_url(self):
        messages.success(self.request, f'"{self.object.title}" foi excluído com sucesso!')
        return reverse('expense:list')    


