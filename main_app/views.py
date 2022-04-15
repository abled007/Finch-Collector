from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     return HttpResponse('Finch Home')

class About(TemplateView):
    template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse('About Finch')

class Finch:
    def __init__(self, name, population, habitat):
        self.name = name
        self.population = population
        self.habitat = habitat

finches = [
    Finch('Painted Bunting', 3.4, 'Scrub'),
    Finch('Black Rosy-Finch', 20000, 'Tundra'),
    Finch('Northern Cardinal', 4.4, 'Woodlands'),
]

class FinchList(TemplateView):
    template_name = "finchList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = finches
        return context