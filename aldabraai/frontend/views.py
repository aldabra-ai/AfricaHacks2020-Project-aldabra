from django.shortcuts import render
from django.views.generic import TemplateView

class AppVIew(TemplateView):
    template_name = 'frontend/index.html'

