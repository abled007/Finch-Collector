from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Finch
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     return HttpResponse('Finch Home')

class About(TemplateView):
    template_name = "about.html"
    # def get(self, request):
    #     return HttpResponse('About Finch')

class FinchList(TemplateView):
    template_name = "finchList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = Finch.objects.all()
        return context