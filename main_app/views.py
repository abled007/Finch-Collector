from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     return HttpResponse('Finch Home')

class About(TemplateView):
    template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse('About Finch')

class Finch_Create(CreateView):
    model = Finch
    fields = ['name', 'population', 'habitat']
    template_name = 'finch_create.html'
    # success_url = '/finch/'
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})  

class FinchDetail(DetailView):
    model = Finch
    template_name = 'finch_detail.html'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'population', 'habitat']
    template_name = 'finch_update.html'
    # success_url = '/finch'
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})


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