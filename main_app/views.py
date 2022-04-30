from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Finch, FinchToy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Finch_Create(CreateView):
    model = Finch
    fields = ['name', 'population', 'habitat']
    template_name = 'finch_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/finch')

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})  

def profile(request, username):
    user = User.objects.get(username=username)
    finches = Finch.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'finches': finches})

class FinchDetail(DetailView):
    model = Finch
    template_name = 'finch_detail.html'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'population', 'habitat']
    template_name = 'finch_update.html'

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

class FinchDelete(DeleteView):
    model = Finch
    template_name = 'finch_delete_confirmation.html'
    success_url = '/finch/'

def finchtoy_index(request):
    finchtoys = FinchToy.objects.all()
    return render(request, 'finchtoy_index.html', {'finchtoys': finchtoys})

def finchtoy_show(request, finchtoy_id):
    finchtoy = FinchToy.objects.get(id=finchtoy_id)
    return render(request, 'finchtoy_show.html', {'finchtoy': finchtoy})

class FinchToyCreate(CreateView):
    model = FinchToy
    fields = '__all__'
    template_name = "finchtoy_form.html"
    success_url = '/finchtoy'

class FinchToyUpdate(UpdateView):
    model = FinchToy
    fields = ['name', 'color']
    template_name = "finchtoy_update.html"
    success_url = '/finchtoy'

class FinchToyDelete(DeleteView):
    model = FinchToy
    template_name = "finchtoy_confirm_delete.html"
    success_url = '/finchtoy'
    
class FinchList(TemplateView):
    template_name = "finchList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['finches'] = Finch.objects.filter(name__icontains=name)
            context['header'] = f'Searching for {name}'
        else:
            context["finches"] = Finch.objects.all()
            context['header'] = 'Our Finches'
        return context