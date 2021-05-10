from django.http import request, response
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
import requests
from requests.auth import HTTPBasicAuth


# def home(request):
#     response = requests.get(f'http://127.0.0.1:3000/api/v1/accounts/patients/1')
#     patient = response.json()

#     return render(request, 'index.html', {
#         'patient': patient
#         })


def home(request):
    return render(request, 'home/home.html')