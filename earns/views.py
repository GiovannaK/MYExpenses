from django.shortcuts import render
from .models import Category, Earns
from profiles.models import Profile
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class EarnsListView(LoginRequiredMixin, ListView):
    model = Earns
    template_name = 'earns/earnings.html'
    context_object_name = 'earns'
    paginate_by = 6
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




