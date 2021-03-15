from django.urls import path
from .views import AppVIew

urlpatterns = [
    path('', AppVIew.as_view(), name='app')
]
