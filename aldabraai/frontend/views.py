from django.shortcuts import render
from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = 'frontend/index.html'

class LandingPage(TemplateView):
    template_name = 'frontend/landing.html'