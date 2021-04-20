from django.urls import path
from .views import AppVIew

app_name = 'frontend'

urlpatterns = [
    path('', AppVIew.as_view(), name='app-view')
]
