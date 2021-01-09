from django.urls import path
from . import views

urlpatterns = [
    #path('', views.IndexPage.as_view(), name='index-page'),
    path('', views.LandingPage.as_view(), name='home')
]
